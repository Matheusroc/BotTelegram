import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, CallbackContext, ContextTypes



async def tabela(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Atualmente temos cursos de:
        /V1 | ???
        /V2 | ???
        /V3 | ???
        /V4 | ???
        /V5 | ???
        """
    )