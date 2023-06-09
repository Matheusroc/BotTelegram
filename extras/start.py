import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters, MessageHandler




#########################
#                       #
# CMD de start e /start #
#                       #
#########################


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Olá, sou um bot que estou em desenvolvimento, e meu objetivo é ter armazernado cursos, e lhe passar por video. ** Não sabemos se liberaremos para o público ainda ** "
    )