# -*- coding: utf-8 -*-
from flask import jsonify
from data_handler import append_data_point, get_top_five_strings_from_stack

def save_station_data(content):
    station = content['station']
    date_and_time = content['time']
    number_of_bikes = content['bikes']

    append_data_point(station, [date_and_time, number_of_bikes])

def get_five_last_answers():
    messages_list = get_top_five_strings_from_stack()
    return jsonify({'messages': messages_list})