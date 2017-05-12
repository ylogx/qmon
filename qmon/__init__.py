"""
QMonination Helper

@author Shubham Chaudhary
@email me@shubhamchaudhary.in
"""
from pkg_resources import get_distribution, DistributionNotFound


__title__ = 'qmon - Redis Monitor'
__author__ = 'Shubham Chaudhary'
__license__ = 'GPLv3+'
__copyright__ = 'Copyright 2017 Shubham Chaudhary'
try:
    __version__ = get_distribution('qmon').version
except DistributionNotFound:
    __version__ = '0.0.1'
