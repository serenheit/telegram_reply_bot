#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from google.appengine.ext import db
from google.appengine.ext import vendor
# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
vendor.add('lib')

import config
import datetime
import random
import logging
import telegram
from fuzzywuzzy import fuzz
from flask import Flask, request

app = Flask(__name__)

global bot
bot = telegram.Bot(token=config.token)

log = logging.getLogger()

RESPONSES_TYPES = ["text", "sticker"]
    
class Response(db.Model):
    name = db.StringProperty()
    resp_type = db.StringProperty(choices=RESPONSES_TYPES)
    resp_value = db.StringProperty()
    limit_burst = db.FloatProperty()
    limit_rate  = db.FloatProperty()
  
def match_index(s, l):
    score = 0
    result = ""

    if l is None:
        return ('', 0)
    
    for item in l:
        if item.lower() in s.lower():
            return (item, 100)
    
    sc = 0
    for item in l:
        sc = fuzz.WRatio(s, item, force_ascii=False)
        if sc > score:
            score = sc
            result = item
    return (result, score)
  
@app.route('/' + config.token, methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))
        log.debug(update)
        if not update.message:
            return "ok"

        chat_id = update.message.chat.id
        
        if update.message.new_chat_member and \
                update.message.new_chat_member.username != config.bot_username:
            bot.sendMessage(chat_id=chat_id,
                    text=config.new_person_text,
                    reply_to_message_id=update.message.message_id)
        elif update.message.left_chat_member and \
                update.message.left_chat_member.username != config.bot_username:
            bot.sendMessage(chat_id=chat_id,
                    text=config.person_left_text,
                    reply_to_message_id=update.message.message_id)
        elif update.message.from_user.username != config.bot_username and \
                len(update.message.text) >= config.min_text_len:
            text = update.message.text
            if update.message.from_user.username == config.admin_username and\
                    text.startswith(config.admin_message_start): # admin message

                command = text.split(" ", 2) # TODO: Split to argparse
                try:
                    if command[1] == "add":
                        lines = command[2].split('"') #"string" "type" "value" "burst" "rate"
                        response = Response(
                                name = lines[1],
                                resp_type = lines[3],
                                resp_value = lines[5],
                                limit_burst = 0.0,
                                limit_rate = 0.0) # TODO limits
                        response.put()
                except IndexError:
                    log.debug("Invalid command parameters")
                    bot.sendMessage(chat_id=chat_id,
                            text="I tried, but failed, my lord",
                            reply_to_message_id=update.message.message_id)
                except db.BadValueError:
                    log.debug("Invalid quotes")
                    bot.sendMessage(chat_id=chat_id,
                            text='I\'m almost sure it\'s wrong quotes',
                            reply_to_message_id=update.message.message_id)
                else:
                    bot.sendMessage(chat_id=chat_id,
                            text="Yes, my lord",
                            reply_to_message_id=update.message.message_id)
            else:
                result = Response.all().run()
                keys = []
                for x in result:
                    keys.append(x.name)

                leven = match_index(update.message.text, keys)
                log.debug(leven)

                if leven[1] > 75:
                    result = Response.all().filter("name =", leven[0]).run()
                    arr = []
                    for response in result:
                        arr.append((response.resp_type, response.resp_value))
                    t, data = random.choice(arr)

                    if t == "text":
                        bot.sendMessage(chat_id=chat_id,
                                text=data,
                                reply_to_message_id=update.message.message_id)
                    elif t == "sticker":
                        bot.sendSticker(chat_id=chat_id, sticker=data)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook(config.webhook_base + config.token)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/', methods=['GET'])
def index():
    return '.'
