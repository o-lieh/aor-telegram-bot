
import asyncio
import sys
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update

# این خط مخصوص ویندوز است
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

TOKEN = "8405267225:AAEZR3vOM7tKTMf7IJyG-vES0SoFh5ywtTM"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    with open("names.txt", "a", encoding="utf-8") as f:
        f.write(name + "\n")
    await update.message.reply_text(f"{name} عزیز، خوش اومدی!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply))

app.run_polling()
