#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import time

import hypchat

import qmon.status

logger = logging.getLogger(__name__)
TIME_GAP_IN_SECONDS = 5 * 60
APPROX_QUEUE_SIZE = 1e10
NUM_ITEMS_BEFORE_NOTIFY_TOLERANCE = 500


def notify(message, items_in_queue, last_notify_items_length, room):
    def __should_i_notify_subscribers_now():
        return items_in_queue - last_notify_items_length > NUM_ITEMS_BEFORE_NOTIFY_TOLERANCE

    should_notify = __should_i_notify_subscribers_now()
    # echo $MSG | mutt -s "Ratings Queue Monitoring - $ITEMS" shubham.chaudhary@zomato.com

    room.notification(
        message,
        color='green' if should_notify else 'gray',  # yellow, green, red, purple, gray, random
        notify=should_notify
    )
    logger.info('{:s}. Items: {:,d}. Last Notify: {:,d}'.format(message, items_in_queue, last_notify_items_length))
    return should_notify


def monitor_queue(queue_name, host, port, room, sleep_time=TIME_GAP_IN_SECONDS, stop_once_empty=False):
    sleep_time = int(sleep_time)
    if sleep_time < 1:
        raise ValueError('Sleep time too low. Please specify sleep time in seconds.')
    if room is None:
        raise ValueError('Please specify a valid room name')
    logger.info('Connecting to hipchat')
    hip_token = os.environ['HIP_TOKEN']  # Please specify your token using: export HIP_TOKEN=my_hipchat_token
    hc = hypchat.HypChat(hip_token)
    room = hc.get_room(room)

    room.notification(
        'Starting to monitor queue={queue} on port={port}'.format(queue=queue_name, port=port),
        color='yellow',  # yellow, green, red, purple, gray, random
        notify=True
    )

    items_in_queue = APPROX_QUEUE_SIZE
    last_notify_items_length = 0
    last_items_length = 0
    rd = qmon.status.redis_connection_cached(host, port)
    while not stop_once_empty or items_in_queue:
        items_in_queue = qmon.status.get_items_in_queue(queue_name, redis_conn=rd, default=0)
        if last_items_length != items_in_queue:
            message = '{} queue status: {:,d}'.format(queue_name, items_in_queue)

            notified = notify(message, items_in_queue, last_notify_items_length, room)
            if notified:
                last_notify_items_length = items_in_queue
            last_items_length = items_in_queue
        time.sleep(sleep_time)

    room.notification(
        'All done for {queue}.'.format(queue=queue_name),
        color='yellow',  # yellow, green, red, purple, gray, random
        notify=True
    )
