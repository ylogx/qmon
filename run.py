#!/usr/bin/env python3
# coding=utf-8

import sys

from qmon import main

try:
    main.setup_logging()
    sys.exit(main.main())
except KeyboardInterrupt:
    sys.exit(1)
