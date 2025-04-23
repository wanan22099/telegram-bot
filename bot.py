import os
from telegram import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Update
)
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters
)

TOKEN = os.environ.get("TOKEN")

def start(update: Update, context: CallbackContext):
    # 固定菜单（ReplyKeyboardMarkup）
    menu_buttons = [
        ["📚 文档", "🛠️ 工具"],
        ["🌐 官网", "❓ 帮助"]
    ]
    reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)

    # 发送带固定菜单的消息
    update.message.reply_text(
        "请选择操作：",
        reply_markup=reply_markup
    )

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if text == "📚 文档":
        # 内联键盘（带链接按钮）
        keyboard = [
            [InlineKeyboardButton("官方文档", url="https://core.telegram.org/bots/api")],
            [InlineKeyboardButton("GitHub 源码", url="https://github.com/python-telegram-bot/python-telegram-bot")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            "请选择文档：",
            reply_markup=reply_markup
        )
    elif text == "🌐 官网":
        update.message.reply_text("官网链接：https://example.com")
    else:
        update.message.reply_text("未知命令")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # 注册命令和消息处理器
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
