import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters, MessageHandler
import yt_dlp
from config import config

videos = [
     # so pode ser video de ate 10 minutos
    "https://youtu.be/xFkTVNKsNqM"
     
]

async def Curso1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(caption="opa",photo='AgACAgQAAxkDAAICS2R9JWCNm37MmmQ34Os254Uq9ZSgAAKUrzEbc-CkUsC1oSFcOiU7AQADAgADcwADLwQ')
    print("Video 1 - Ok")
    print("-----------------------------------------------------------------")
    await update.message.reply_video(caption="opa",video='BAACAgQAAxkDAAICXWR9poWr3WB7SKfabC6g5he3ZhOvAALlAwACkiD0Uy-25Pu9Sm62LwQ')
    print("Video 2 - ok")
    print("-----------------------------------------------------------------")
    await update.message.reply_video(caption="opa",video='BAACAgQAAxkDAAICeWR9qS8DjhUXmElK2RUAAVMOTWLH_QACxwMAAkTA9VM1Ulj7q58wjC8E')
    print("Video 3 - ok")
    print("-----------------------------------------------------------------")
    await update.message.reply_video(caption="opa",video='AgACAgEAAx0CaeV8BAADCmSDcxSjKqJPVrxcgAf5nmruL1e7AAJJqzEb7YoYRCM38iLjzMjdAQADAgADeQADLwQ')
    print("Video 4 - ok")
    print("-----------------------------------------------------------------")


    for video in videos:
      try:
            downloader = yt_dlp.YoutubeDL(
              {'format': 'best', 'title': True, "cookiefile": config.COOKIE_PATH})
            r = downloader.extract_info(video, download=False)
      except:
            asyncio.wait(1)
            downloader = yt_dlp.YoutubeDL(
              {'title': True, "cookiefile": config.COOKIE_PATH})
            r = downloader.extract_info(
              video, download=False)
      stream_url = r.get("url")
      p = await update.message.reply_video(video=stream_url)
      print(p)

    # await application.send_document(chat_id=, document='https://python-telegram-bot.org/static/testfiles/telegram.gif')
    # await update.message.reply_document(chat_id=update.effective_chat.id, document = "AgACAgEAAxkBAAEiAxVke_3HrUjdl6WSUPEOOltVbpSJeAAClKsxGwmB4UcHOXpFeu5HjgEAAwIAA3gAAy8E")
    # await update.message.reply_video(video='./videos/tt.mp4')

