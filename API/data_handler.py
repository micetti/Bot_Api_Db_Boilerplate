# -*- coding: utf-8 -*-
from redis import Redis

COUNTER_KEY = 'hits'
LIST_KEY = 'message_list'

redis = Redis(host='redis', port=6379)

def increment_counter():
    return redis.incr(COUNTER_KEY)

def get_counter_value():
    return int(redis.get(COUNTER_KEY))

def save_string_on_top_of_stack(message_string):
    redis.lpush(LIST_KEY, message_string)

def get_top_five_strings_from_stack():
    byte_string_list = redis.lrange(LIST_KEY, 0, 4)
    string_list = []
    for bytes_string in byte_string_list:
        string_list.append(str(bytes_string,'utf-8'))
    return string_list
