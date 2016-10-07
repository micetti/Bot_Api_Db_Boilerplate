# -*- coding: utf-8 -*-
from flask import jsonify
from data_handler import increment_counter, get_counter_value, save_string_on_top_of_stack, get_top_five_strings_from_stack

HELLO_WORLD = "Hello World"

def answer_hello_world():
    return HELLO_WORLD

def increase_counter_and_inform():
    increment_counter()
    return "You are visitor number {}".format(get_counter_value())

def save_message(content):
    try:
        message_string = content['message']
        save_string_on_top_of_stack(message_string)
    except:
        return

def get_five_last_answers():
    messages_list = get_top_five_strings_from_stack()
    return jsonify({'messages': messages_list})