# -*- coding: utf-8 -*-
import requests
import re

API_ENDPOINT = 'http://api:5000/'

PUT = re.compile('/put', re.I)
LIST = re.compile('/list', re.I)
HELP = re.compile('/help', re.I)
NAME = re.compile('/name', re.I)
FLAT = re.compile('/flat', re.I)

def send_message_and_get_echo(message, chat_id):
    if PUT.match(message):
        result = requests.post(API_ENDPOINT + 'put/', json={'message': message, 'chat_id': chat_id})
        return result.json()['messages']

    if LIST.match(message):
        result = requests.post(API_ENDPOINT + 'list/', json={'message': message, 'chat_id': chat_id})
        return result.json()['messages']

    if HELP.match(message):
        return HELP_TEXT

    if NAME.match(message):
        result = requests.post(API_ENDPOINT + 'name/', json={'message': message, 'chat_id': chat_id})
        return result.json()['messages']

    if FLAT.match(message):
        tmp = message.split(' ')
        if len(tmp) != 2:
            return ['Please use the format /flat myFlat in order to join or create myFlat']
        flat_name = tmp[1]
        result = requests.post(API_ENDPOINT + 'flat/', json={'message': flat_name, 'chat_id': chat_id})
        return result.json()['messages']

    return ['command not found']

HELP_TEXT = [
    'Supported commands are:',
    '/put 17.08 - This will add 17.08 Euro to your account',
    '/list - This will show the balance of all people in your flat',
    '/name John - This will set your name, shown to others of the flat, to John',
    '/flat myFlat - This will create the flat myFlat or let you join it if exists'
]