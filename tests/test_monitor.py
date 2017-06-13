# -*- coding: utf-8 -*-
import unittest
from unittest import mock

from qmon.monitor import monitor_queue


@mock.patch('qmon.monitor.time.sleep')
@mock.patch('qmon.monitor.os.environ')
@mock.patch('qmon.monitor.hypchat.HypChat')
@mock.patch('qmon.monitor.qmon.status.get_items_in_queue')
@mock.patch('qmon.monitor.qmon.status.redis_connection_cached')
class TestMonitor(unittest.TestCase):
    def setup_mock(self, mock_hypchat, mock_items_in_queue, mock_os, mock_redis, items_in_queue=None):
        if not items_in_queue:
            items_in_queue = [0]
        mock_items_in_queue.side_effect = items_in_queue
        redis = mock.MagicMock()
        mock_redis.return_value = redis
        mock_os.__getitem__.return_value = 'dummy_token'
        client = mock.MagicMock()
        room = mock.MagicMock()
        client.get_room.return_value = room
        mock_hypchat.return_value = client
        return room

    def test_monitor_queue__no_items__only_start_notification_and_end_notification(
            self, mock_redis, mock_items_in_queue, mock_hypchat, mock_os, mock_sleep
    ):
        room = self.setup_mock(mock_hypchat, mock_items_in_queue, mock_os, mock_redis, items_in_queue=[0])

        monitor_queue(
            'dummy_queue',
            'dummy_host',
            10,
            'dummy_room',
            stop_once_empty=True,
        )

        room.notification.assert_has_calls([
            mock.call('Starting to monitor queue=dummy_queue on port=10', color='yellow', notify=True),
            mock.call('All done for dummy_queue.', color='yellow', notify=True),
        ])
        self.assertEqual(2, room.notification.call_count)

    def test_monitor_queue__some_items__send_notification(
            self, mock_redis, mock_items_in_queue, mock_hypchat, mock_os, mock_sleep
    ):
        room = self.setup_mock(mock_hypchat, mock_items_in_queue, mock_os, mock_redis, items_in_queue=[30, 0])

        monitor_queue(
            'dummy_queue',
            'dummy_host',
            10,
            'dummy_room',
            stop_once_empty=True,
        )

        room.notification.assert_has_calls([
            mock.call('dummy_queue queue status: 30', color='gray', notify=False),
            mock.call('dummy_queue queue status: 0', color='gray', notify=False),
        ])
        self.assertEqual(4, room.notification.call_count)
