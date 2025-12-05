from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8405267225:AAEZR3vOM7tKTMf7IJyG-vES0SoFh5ywtTM"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    # ذخیره اسم در فایل
    with open("names.txt", "a", encoding="utf-8") as f:
        f.write(name + "\n")
    await update.message.reply_text(f"{name} عزیز، خوش اومدی!")

# ساخت بات با ApplicationBuilder
app = ApplicationBuilder().token(TOKEN).build()

# اضافه کردن handler برای پیام‌های متنی
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply))

# اجرای بات (polling)
app.run_polling()