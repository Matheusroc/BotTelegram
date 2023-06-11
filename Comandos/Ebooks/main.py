import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def Ebooks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(parse_mode="HTML", chat_id=update.effective_chat.id, 
    text="""
    Pai rico pai pobre:
    <a href="https://drive.google.com/u/0/uc?id=1lfuy_O4UrSAChBEu2DS9vg2wAFtcwnnm&export=download" download="Arquivo.pdf">Download</a>""")
