# -*- coding: utf-8 -*-
from redis import Redis

LIST_KEY = 'message_list'

redis = Redis(host='redis', port=6379)

def append_data_point(id, data):
    redis.rpush(id, data)

def get_top_five_strings_from_stack():
    byte_string_list = redis.lrange('87', 0, 4)
    string_list = []
    for bytes_string in byte_string_list:
        string_list.append(str(bytes_string,'utf-8'))
    return string_list

def get_flat(flat_name):
    return redis.get(flat_name)