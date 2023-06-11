import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters, MessageHandler
import yt_dlp
from config import config


async def V1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_video(caption="""
                #Bloco001

                1 Como Estudar por aqui
                00:00:00 1  Seja Bem Vindo! Vamos aprender a detectar faces!  509K
                00:03:44 2  Como estudar nessa plataforma_  435K

                2 A Face
                00:08:08 1  O que é nossa face_  541K
                00:10:35 2  Face, uma origem de nossos ancestrais_  566K
                00:13:51 3  Emoções na Face_  570K
                00:17:35 4  O que nossa face revela_  509K

                3 Micro Expressões Faciais
                00:28:16 1  Macro Expressão Facial_  502K
                00:30:52 2  O que são _Micro expressões _faciais__  538K
                00:33:06 3  Tempo e intensidade da contração facial  524K
                00:35:48 4  Simetria vs Assimetria  541K
                00:37:49 5  Intensidade Gradual  492K
                00:39:49 6  Sincronia dos músculos da face  547K
                00:41:34 7  Combinações e Códigos Faciais  540K....

""",video='BAACAgEAAx0CaeV8BAAD12SDylkWCPVVKer8Js28EDQwm4lEAAI4BAACCU0hRLlqJJV6Hll9LwQ')
    print("Video 1 - Ok")
    print("-----------------------------------------------------------------")