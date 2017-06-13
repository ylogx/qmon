#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   main.py - All commandline interactions
#   This file is a part of QMon.
#
#   Copyright (c) 2017 Shubham Chaudhary <me@shubhamchaudhary.in>
#
#   QMon is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   QMon is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with QMon. If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import print_function

import logging
from argparse import ArgumentParser

import qmon.monitor
from qmon import __version__
from qmon import monitor


def print_version():
    print('QMon version %s' % __version__)
    print('Copyright (c) 2017 by Shubham Chaudhary.')
    print('License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>')
    print('This is free software: you are free to change and redistribute it.')
    print('There is NO WARRANTY, to the extent permitted by law.')


def parse_known_args():
    """ Parse command line arguments """
    parser = ArgumentParser()
    parser.add_argument('--queue-name', '-q', required=True, help='Name of queue')
    parser.add_argument('--host', required=True, help='Redis host')
    parser.add_argument('--port', '-p', help='Redis port')
    parser.add_argument('--room', '-r', help='HipChat Room')
    parser.add_argument('--sleep-time', '-t', default=monitor.TIME_GAP_IN_SECONDS, help='Number of seconds to sleep')
    parser.add_argument('--stop-once-empty', '-s', action='store_true', help='Stop when no items left in queue')
    parser.add_argument('-V', '--version',
                        action='store_true',
                        dest='version',
                        help='Print the version number and exit')
    args, otherthings = parser.parse_known_args()
    return args, otherthings, parser


def main():
    args, otherthings, parser = parse_known_args()

    setup_logging()
    qmon.monitor.monitor_queue(
        queue_name=args.queue_name,
        host=args.host,
        port=args.port,
        room=args.room,
        sleep_time=args.sleep_time,
        stop_once_empty=args.stop_once_empty
    )
    return 0


def setup_logging():
    logging.basicConfig(format='[%(name)s] [%(asctime)s] %(levelname)s : %(message)s')
    logging.getLogger('root').setLevel(logging.DEBUG)
    logging.getLogger('qmon').setLevel(logging.DEBUG)
    logging.getLogger('qmon.monitor').setLevel(logging.DEBUG)


if __name__ == '__main__':
    import sys

    setup_logging()
    sys.exit(main())
