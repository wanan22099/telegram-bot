import os
from telegram import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Update
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters  # 注意是小写！
)

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 固定菜单
    menu_buttons = [["📚 文档", "🌐 官网"]]
    reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)
    await update.message.reply_text("请选择：", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📚 文档":
        # 内联键盘（带链接）
        keyboard = [
            [InlineKeyboardButton("官方文档", url="https://core.telegram.org/bots/api")],
            [InlineKeyboardButton("GitHub", url="https://github.com")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("选择文档：", reply_markup=reply_markup)
    elif text == "🌐 官网":
        await update.message.reply_text("官网链接：https://example.com")

def main():
    # 新版本使用 Application
    application = Application.builder().token(TOKEN).build()
    
    # 注册处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # 启动Bot
    application.run_polling()

if __name__ == "__main__":
    main()
