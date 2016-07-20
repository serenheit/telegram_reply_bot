#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Token you received from BotFather
token = '<token>'

# Text for every new person
new_person_text = 'Greeting Message\n\
Any answer can be multistring'

# Text when someone has left
person_left_text = 'Leave me alone!'

# Bot username. We need it to skip bot's messages (so there will be no loop)
bot_username = 'samplereplybot'

# admin username. This person will be able to add replies to the bot
admin_username = '<your username>'

# messages started with this prefix AND from admin will be parsed as admin messages
# samples:
# To reply to a message with a sticker:
# where the last one is the sticker id, you can get it from logs
# when someone has posted a sticker
# <prefix> add "sample_text" "sticker" "BQADAgADBBBB3-HkAcgB4YAAAAAAAA"
# <prefix> add "another_sample_text" "sample_text" "Funny reply from bot"
# You can add many responses to a single message: bot will pick random
admin_message_start = 'manage '

# URL where the bot is going to answer to the telegram queries
# This URL is passed to Telegram Servers once you called <webhook_base>/set_webhook
webhook_base = '<Bot URL>'

# Minimum message length. Short messages provide strange results for fuzzywuzzy
min_text_len = 5
