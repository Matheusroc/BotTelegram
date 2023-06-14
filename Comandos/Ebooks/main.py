import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def Ebooks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await context.bot.send_message(parse_mode="HTML", chat_id=update.effective_chat.id, 
    text="""
    Pai rico pai pobre:
    <a href="https://drive.google.com/u/0/uc?id=1lfuy_O4UrSAChBEu2DS9vg2wAFtcwnnm&export=download" download="Arquivo.pdf">Download</a>
    """)

    await context.bot.send_message(parse_mode="HTML", chat_id=update.effective_chat.id, 
    text="""
    Fluxo de api:
    <a href="https://drive.google.com/u/0/uc?id=1465jDoLqcH244vtXDAKOBGTmVhiajHfB&export=download" download="Arquivo.pdf">Download</a>
    """)

    await context.bot.send_message(parse_mode="HTML", chat_id=update.effective_chat.id, 
    text="""
    Os 10 principios que todo programador deveria saber:
    <a href="https://drive.google.com/u/0/uc?id=1W6mZzA6m10aoI12Pkw2XnQmu3-Cb9dma&export=download" download="Arquivo.pdf>Download</a>
    """)

    await context.bot.send_message(parse_mode="HTML", chat_id=update.effective_chat.id, 
    text="""
    Comandos importantes GIT:
    <a href="https://drive.google.com/u/0/uc?id=1uUfIbSBcRLP8PELmAs5n-3ng8Lt3tLZV&export=download" download="Arquivo.pdf">Download</a>
    """)
    await context.bot.send_message(parse_mode="HTML", chat_id=update.effective_chat.id, 
    text="""
    Fundamentos do React:
    <a href="https://drive.google.com/u/0/uc?id=10dOKXDQhrONLebNE-7J_P5Qt6J9dOMh8&export=download" download="Arquivo.pdf">Download</a>
    """)
    await context.bot.send_message(parse_mode="HTML", chat_id=update.effective_chat.id, 
    text="""
    Os segredos do Java Script:
    <a href="https://drive.google.com/u/0/uc?id=1WLTX-b-9k1FTweSvYon6tgzDz1VvXRWG&export=download" download="Arquivo.pdf">Download</a>
    """)
    await context.bot.send_message(parse_mode="HTML", chat_id=update.effective_chat.id, 
    text="""
    Melhores praticas para HTML e CSS:
    <a href="https://drive.google.com/u/0/uc?id=1MRbfyW3ui2TgmI1muP9PVg5t6JWLh_CW&export=download" download="Arquivo.pdf">Download</a>
    """)