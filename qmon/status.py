# -*- coding: utf-8 -*-
from redis import StrictRedis

_redis = None


def redis_connection_cached(host, port):
    global _redis
    if _redis is None:
        _redis = redis_connection(host=host, port=port)
    return _redis


def redis_connection(host, port):
    return StrictRedis(host=host, port=port)


def get_items_in_queue(queue_name, redis_conn, default=None):
    type_name = redis_conn.type(queue_name).decode()
    if type_name == 'hash':
        length_op = redis_conn.hlen
    elif type_name == 'list':
        length_op = redis_conn.llen
    elif type_name == 'set':
        length_op = redis_conn.scard
    elif type_name == 'none' and default is not None:
        length_op = lambda _: default
    else:
        raise ValueError('Queue empty or Unknown type_name "{}" of queue "{}"'.format(type_name, queue_name))
    return length_op(queue_name)
