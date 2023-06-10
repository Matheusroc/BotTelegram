import asyncio
import telegram
import logging
from telegram import Update, PhotoSize
from telegram.ext import Application, ContextTypes, CommandHandler, filters, MessageHandler
import yt_dlp
import json


print("Carregando.")
print("Carregando..")
print("Carregando...")
#########################
#                       #
#  Importe de arquivos  #
#                       #
#########################

#Esta inportando um arquivo curso1.py, ele reconhece como se estivese aqui no arquivo principal, mas, 
# so deixa mais organizado para nos. Com esse inport oi, ele apenas puxa o oi para não dar erro aqui
from tabela import tabela
from extras.erro import unknown
from extras.start import start
from Source.MicroExpressoesFaciais.main import Curso1
from extras.help import help
from Comandos.Util.util import utils
from Comandos.Olhando.main import vendo
from Videos.test.test import testv1

print("Carregado 100%")
#########################
#                       #
#      add o comando    #
#                       #
#########################

# Define a função que será executada quando receber uma mensagem
async def reply(update, context):
    # Obtém as informações da mensagem recebida
    message = update.message
    message_id = message.message_id
    message_date = message.date
    message_text = message.text

    # Cria um dicionário com as informações da mensagem
    message_info = {
        'update_id': update.update_id,
        'message': {
            'message_id': message_id,
            'from': {
                'id': message.from_user.id,
                'is_bot': message.from_user.is_bot,
                'first_name': message.from_user.first_name,
                'username': message.from_user.username,
                'language_code': message.from_user.language_code,
            },
            'chat': {
                'id': message.chat.id,
                'first_name': message.chat.first_name,
                'username': message.chat.username,
                'type': message.chat.type,
            },
            'date': str(message_date),
            'text': message_text,
        }
    }

    if message.photo:
        # Pega a última foto enviada na mensagem
        file_id = message.photo[-1].file_id
        message_info['message']['photo_file_id'] = file_id
    elif message.video:
        file_id = message.video.file_id
        message_info['message']['video_file_id'] = file_id

    # Converte as informações da mensagem em JSON formatado para envio
    message_json = json.dumps(message_info, indent=2)

    # Responde ao usuário com as informações da mensagem
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_json)



if __name__ == '__main__':
    application = Application.builder().token('6149861753:AAGWyyBCofJU3jYKCDUNGT-EyaxxT6hdA2g').build()

    # Passa o manipulador de mensagem para o objeto Updater
    #application.add_handler(MessageHandler(filters.ALL, reply))


    #comando start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    #comando tabela
    tabela_handler = CommandHandler('tabela', tabela) #entre 'tabela' é comando(é o que ele digita), e o do lado é a função(chamar a função)
    application.add_handler(tabela_handler)

    #comando C1
    C1_handler = CommandHandler('Curso1', Curso1)
    application.add_handler(C1_handler)

    #comando testV1
    C1_handler = CommandHandler('testV1', testv1)
    application.add_handler(C1_handler)

    #comando help
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    #comando utils
    utils_handler = CommandHandler('utils', utils)
    application.add_handler(utils_handler)

    #comando vendo
    vendo_handler = CommandHandler('Olhe', vendo)
    application.add_handler(vendo_handler)

    #esse sempre tem que ser o ultimo, pq se colocar em primeiro, ele cancela todos os outros.
    # Comando não encontrado
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    #bot ouve
    application.run_polling()