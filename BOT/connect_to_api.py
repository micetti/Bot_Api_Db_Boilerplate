# -*- coding: utf-8 -*-
import requests

ECHO_ENDPOINT = 'http://api:5000/echo/'

def send_message_and_get_echo(message):
    result = requests.post(ECHO_ENDPOINT, json = {'message': message})
    return result.json()['messages']
