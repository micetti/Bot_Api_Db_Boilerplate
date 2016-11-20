# -*- coding: utf-8 -*-

import time
import telepot
from connect_to_api import send_message_and_get_echo

TOKEN = '272432252:AAGXjxfQTSrIoUIT2pJ5LJfZLhlWCjpzTJY'

def echo(message):
    content_type, chat_type, chat_id = telepot.glance(message)
    if content_type == 'text':
        messages_list = send_message_and_get_echo(message['text'], chat_id)
        for message in messages_list:
            bot.sendMessage(chat_id, message)

if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    bot.message_loop(echo)
    # Keep the program running.
    while 1:
        time.sleep(10)

