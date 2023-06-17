import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, CallbackContext, ContextTypes



async def Tabela(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Atualmente temos:
        /V1 | Micro expressões faciais
        /Ori
            ◜
            /C2_1 Html e CSS para iniciantes
            /C2_2 Ui para iniciantes
            ◞  
        /V3 | ???
        /V4 | ???
        /V5 | ???
        """
    )