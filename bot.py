import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello from Git Bash!')

TOKEN = os.environ.get("TOKEN")  # 从环境变量读取 Token
updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()