# Sample Telegram Replier

* A simple Telegram bot that reacts to specific phrases based on config.

Works with Google Apps Engine and stores the values in its DB

To setup, use instructions for [Sample Telgram Bot](https://github.com/sooyhwang/Simple-Echo-Telegram-Bot) and maybe somewhere over the Internet (Google: Telegram Bot Google App Engine)

After that, set values in config.py and application in app.yaml
I tried to add as many comments, as I could

And I hate Python dependency handling, so you should probably call something like:
```
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/certifi ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/click ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/flask ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/future ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/fuzzywuzzy ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/itsdangerous.py ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/jinja2 ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/markupsafe ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/telegram ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/urllib3 ./
telegram_reply_bot/lib$ ln -s /Library/Python/2.7/site-packages/werkzeug ./
```
