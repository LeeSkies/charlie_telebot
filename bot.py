from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from requests import post
from palm import ask
from data import guard, open_conversation, close_conversation
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN')

async def handle_hoot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hoot? Hoot!")

async def handle_open(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.message.chat
    if chat['username'] != os.environ.get('ADMIN'):
        await update.message.reply_text("Hoot! Hoot!")
        return
    text = update.message.text
    tokens = text.split()
    if len(tokens) != 2:
        await update.message.reply_text(f"Expected 2 tokens. got {len(tokens)}")
        return
    bool = open_conversation(chat_id=tokens[1])
    if bool:
        await update.message.reply_text("Updated")
    elif not bool:
        await update.message.reply_text("Not found")

async def handle_close(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.message.chat
    if chat['username'] != os.environ.get('ADMIN'):
        await update.message.reply_text("Hoot! Hoot!")
        return
    text = update.message.text
    tokens = text.split()
    if len(tokens) != 2:
        await update.message.reply_text(f"Expected 2 tokens. got {len(tokens)}")
        return
    bool = close_conversation(chat_id=tokens[1])
    if bool:
        await update.message.reply_text("Updated")
    elif not bool:
        await update.message.reply_text("Not found")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    chat = update.message.chat
    message = update.message.text
    print(f"{chat['first_name']}: {message}")
    if guard(chat['id']) != True:
        await update.message.reply_text("Hoot! Hoot!")
        return
    answer = ask(str=message, chat_id=chat['id'])
    await update.message.reply_text(answer)

try:
    app = ApplicationBuilder().token(TOKEN).build()
    print("Hoot! Hoot!")
    app.add_handler(CommandHandler('Hoot', handle_hoot))
    app.add_handler(CommandHandler('hoot', handle_hoot))
    app.add_handler(CommandHandler('open', handle_open))
    app.add_handler(CommandHandler('close', handle_close))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling(poll_interval=3)
except Exception as e:
    print(e)
    print("Couldn't start the bot")
