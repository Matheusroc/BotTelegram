import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Vejo que você está com dúvidas, então aqui estão meus comandos: 
        """
    )