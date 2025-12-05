from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "توکن_بات_اینجا"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text

    # ذخیره اسم در فایل
    with open("names.txt", "a", encoding="utf-8") as f:
        f.write(name + "\n")

    await update.message.reply_text(f"{name} عزیز، خوش اومدی!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply))

app.run_polling()

