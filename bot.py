import os
from telegram import (
    ReplyKeyboardMarkup,
    Update,
    KeyboardButton
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 固定菜单按钮（底部输入框下方）
    menu_buttons = [
        [KeyboardButton("📱 小程序", web_app={"url": "https://telegram.me/iv?url=YOUR_WEBAPP_URL"})],
        [KeyboardButton("👥 加入群组", url="https://t.me/your_group")],
        [KeyboardButton("📢 订阅频道", url="https://t.me/your_channel")],
        [KeyboardButton("📞 联系客服", url="https://t.me/your_contact")]
    ]
    reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True, one_time_keyboard=False)
    
    await update.message.reply_text(
        "请点击下方按钮快速访问：",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 处理按钮点击（非必须，仅作响应提示）
    await update.message.reply_text(f"您点击了: {update.message.text}")

def main():
    application = Application.builder().token(TOKEN).build()
    
    # 注册处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()

if __name__ == "__main__":
    main()
