import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters, MessageHandler
import yt_dlp
from config import config


async def Curso1(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
                00:41:34 7  Combinações e Códigos Faciais  540K

""",video='BAACAgEAAx0CaeV8BAAD12SDylkWCPVVKer8Js28EDQwm4lEAAI4BAACCU0hRLlqJJV6Hll9LwQ')
    print("Video 1 - Ok")
    print("-----------------------------------------------------------------")

#                4 Os sinais faciais de cada emoção
                # 00:44:46 1   As Sete Emoções Básicas!  550K
                # 00:49:58 2   Raiva  585K
                # 00:52:43 3   Raiva na face  466K
                # 00:55:15 4   Quais os sinais de Raiva nesse vídeo_  374K
                # 00:55:16 5   Nojo  531K
                # 00:57:06 6   Nojo na face  410K
                # 00:59:10 7   Quais os sinais de nojo nesse vídeo_  298K
                # 00:59:11 8   Quais as emoções de nojo nesse vídeo_  382K
                # 00:59:12 9   Tristeza  534K
                # 01:01:22 10   Tristeza na face  461K
                # 01:03:45 11   Quais os sinais de tristeza nesse vídeo_  303K
                # 01:03:51 12   Desprezo  558K
                # 01:05:30 13   Desprezo na face  467K
                # 01:08:29 14   Quais os sinais de desprezo nesse vídeo_  364K
                # 01:08:31 15   Quais os sinais de Desprezo nesse vídeo_  451K
                # 01:08:32 16   Felicidade  560K
                # 01:10:27 17   Felicidade na face  412K
                # 01:12:01 18   Quais os sinais de felicidade nesse vídeo_  443K
                # 01:12:03 19   Quais os sinais de felicidade nesse vídeo_  388K
                # 01:12:05 20   Surpresa~  567K
                # 01:13:24 21   Surpresa na face.  491K_2
                # 01:14:52 22   Quais os sinais de surpresa nesse vídeo_  411K
                # 01:14:53 23   Quais os sinais de surpresa nesse vídeo_  424K
                # 01:14:54 24   Medo  561K
                # 01:16:29 25   Medo na face.  481K
                # 01:18:45 26   Quais os sinais de medo nesse vídeo_  418K
                # 01:18:46 27   Quais os sinais de medo nesse vídeo_  381K

                # 5 Detectando as expressões!
                # 01:18:47 1   Linha de Base  557K
                # 01:22:39 2   Como realizar os exercícios_  492K
                # 01:25:01 3   Página 1  326K
                # 01:25:08 3.1  Página 1   311K
                # 01:25:18 3.2  Página 1  378K
                # 01:25:31 4   Página 2  350K
                # 01:25:42 4.1  Página 2  358K
                # 01:25:50 4.2   Página 2  306K
                # 01:25:58 5   Página 3  683K
                # 01:26:08 5.1   Página 3   259K
                # 01:26:16 5.2   Página 3  298K
                # 01:26:26 6   Página 4  293K
                # 01:26:32 6.1   Página 4   293K
                # 01:26:41 6.2   Página 4  240K
                # 01:26:49 7   Página 5  260K
                # 01:26:58 7.1   Página 5   419K
                # 01:27:05 7.2   Página 5  358K
                # 01:27:14 8   Página 6  306K
                # 01:27:23 8.1   Página 6   344K
                # 01:27:29 8.2   Página 6  307K
                # 01:27:36 9   Página 7  379K
                # 01:27:42 9.1   Página 7   267K
                # 01:27:50 9.2   Página 7  312K
                # 01:28:00 10   Página 8  271K
                # 01:28:07 10.1   Página 8   381K
                # 01:28:15 10.2   Página 8  366K
                # 01:28:26 11   Página 9  227K
                # 01:28:35 11.1   Página 9   181K
                # 01:28:42 11.2   Página 9  198K
                # 01:28:50 12   Página 10  267K_2
                # 01:29:07 12.1   Página 10   128K
                # 01:29:18 12.2   Página 10  174K
                # 01:29:26 13   Qual lugar da face devo prestar atenção_  546K
                # 01:30:49 14   Página 11  162K
                # 01:30:58 14.1   Página 11   218K
                # 01:31:09 14.2   Página 11  186K
                # 01:31:18 15   Página 12  188K
                # 01:31:30 15.1   Página 12   128K
                # 01:31:40 15.2   Página 12  169K
                # 01:31:49 16   Página 13  284K
                # 01:31:58 16.1   Página 13   210K
                # 01:32:07 16.2   Página 13  167K
                # 01:32:15 17   Página 14  227K
                # 01:32:23 17.1   Página 14   140K
                # 01:32:32 17.2   Página 14  178K
                # 01:32:40 18   Página 15  223K
                # 01:32:48 18.1   Página 15   216K
                # 01:32:57 18.2   Página 15   165K
                # 01:33:05 19   Página 16  360K_2
                # 01:33:14 19.1   Página 16   267K
                # 01:33:23 19.2   Página 16  187K
                # 01:33:32 20   Página 17  197K
                # 01:33:40 20.1   Página 17   335K
                # 01:33:48 20.2   Página 17  236K
                # 01:33:56 21   Página 18  198K
                # 01:34:05 21.1   Página 18   159K
                # 01:34:14 21.2   Página 18  595K
                # 01:34:23 22   Página 19  245K
                # 01:34:32 22.1   Página 19   227K
                # 01:34:41 22.2   Página 19  220K
                # 01:34:49 23   Página 20  210K
                # 01:34:58 23.1   Página 20   327K
                # 01:35:07 23.2   Página 20  263K    

