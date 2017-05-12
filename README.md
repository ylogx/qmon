qmon - Redis Monitor
====================

[![Join the chat at https://gitter.im/shubhamchaudhary/qmon](https://badges.gitter.im/shubhamchaudhary/qmon.svg)](https://gitter.im/shubhamchaudhary/qmon?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![PyPI Version](https://img.shields.io/pypi/v/qmon.svg)](https://pypi.python.org/pypi/qmon) [![PyPI Monthly Downloads](https://img.shields.io/pypi/dm/qmon.svg)](https://pypi.python.org/pypi/qmon) [![PyPI License](https://img.shields.io/pypi/l/qmon.svg)](https://pypi.python.org/pypi/qmon) [![GitHub tag](https://img.shields.io/github/tag/shubhamchaudhary/qmon.svg)](https://github.com/shubhamchaudhary/qmon/releases) [![GitHub release](https://img.shields.io/github/release/shubhamchaudhary/qmon.svg)](https://github.com/shubhamchaudhary/qmon/releases/latest)

[![Build Status Travis-CI](https://travis-ci.org/shubhamchaudhary/qmon.svg)](https://travis-ci.org/shubhamchaudhary/qmon) [![Coverage Status](https://coveralls.io/repos/shubhamchaudhary/qmon/badge.svg?branch=master)](https://coveralls.io/r/shubhamchaudhary/qmon?branch=master) [![Circle CI](https://circleci.com/gh/shubhamchaudhary/qmon.svg?style=svg)](https://circleci.com/gh/shubhamchaudhary/qmon) [![Requirements Status](https://requires.io/github/shubhamchaudhary/qmon/requirements.svg?branch=master)](https://requires.io/github/shubhamchaudhary/qmon/requirements/?branch=master)

[![GitHub issues](https://img.shields.io/github/issues/shubhamchaudhary/qmon.svg?style=plastic)](https://github.com/shubhamchaudhary/qmon/issues) [![Stories in Ready](https://badge.waffle.io/shubhamchaudhary/qmon.png?label=ready&title=Ready)](https://waffle.io/shubhamchaudhary/qmon)

QMon is a redis queue monitor 

# Installation
```shell
pip3 install qmon
```


# Usage:

```shell
> export HIP_TOKEN=MyHipChatToken
> qmon --host localhost --port 6379 --queue-name a_key_in_redis --room RoomInHipChat
[qmon.monitor] [2017-05-12 12:36:45,248] INFO : Connecting to hipchat
[qmon.monitor] [2017-05-12 12:36:47,292] INFO : a_key_in_redis queue status: 6. Items: 6. Last Notify: 0
[qmon.monitor] [2017-05-12 12:37:07,754] INFO : a_key_in_redis queue status: 11. Items: 11. Last Notify: 0
[qmon.monitor] [2017-05-12 12:37:20,237] INFO : a_key_in_redis queue status: 16. Items: 16. Last Notify: 0
[qmon.monitor] [2017-05-12 12:37:38,235] INFO : a_key_in_redis queue status: 10. Items: 10. Last Notify: 0
```

This is how it'll appear in hipchat:  
![hipchat_window](http://i.imgur.com/G1vnPUm.png)


Find us:
  * [PyPi](https://pypi.python.org/pypi/qmon)   
