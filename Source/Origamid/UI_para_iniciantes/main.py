import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters, MessageHandler
import yt_dlp



async def C2_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_video(caption="""
        #Materiais001

        02_HTML_e_CSS_para_Iniciantes-001.rar


        #Block001

        01  HTL e CSS para Iniciantes
        00:00:00 0101 HTML e CSS para Iniciantes
        00:08:41 0102 HTML, CSS e JavaScript
        00:18:40 0103 Editor de Código
        00:26:38 0104 Browser
        """,
    video='BAACAgEAAx0CaeV8BAAD_2SFGm-j5_OdWAjChDO8QthguXWNAALqBAACspcxRIgz4l529lVoLwQ')
    print("Video 1 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption="""
        #Block002

        02  HTL e CSS Básico
        00:00:00 0201 Tag
        00:08:04 0202 Tags Iniciais
        00:12:38 0203 Estrutura HTML
        00:17:46 0204 Editor Plugins
        00:32:38 0205 Editor Atalhos
        00:40:35 0206 Link Caminhos
        00:48:41 0207 CSS Básico
        00:55:33 0208 CSS Seletores
        01:06:49 0209 HTML Exercício
        01:20:08 0210 Background e Cores
        01:30:52 0211 Box Model 1
        01:35:52 0211 Box Model 2
        01:47:29 0212 Estilos do Browser""",
    video='BAACAgEAAx0CaeV8BAACAQFkhRvtJL-PTn58V3m-kyfkEs726gAC6wQAArKXMURuR7VcAV7AXC8E')
    print("Video 2 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
            
        #Block003

        02  HTL e CSS Básico
        00:00:00 0213 Display
        00:09:42 0214 Display Exercício
        00:21:34 0215 Documentação
        00:25:24 0216 Imagens 1
        00:33:26 0216 Imagens 2
        """,
    video='BAACAgEAAx0CaeV8BAACARdkhSIhLENEVpwCmh3WZ0gAAT-EhIIAAvUEAAKylzFE8S7b7e8-Kx0vBA')
    print("Video 3 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
        #Block004

        03  CSS Posicionamento
        00:00:00 0301 Top, Right, Bottom, Left
        00:06:26 0302 Grid Columns 1
        00:11:41 0302 Grid Columns 2
        00:20:40 0303 Align e Justify Content
        00:32:46 0304 Grid Column 1
        00:37:56 0304 Grid Column 2
        00:43:08 0305 Align e Justify Items
        00:50:46 0306 Grid Template Rows
        01:02:58 0307 Flexbox 1
        01:10:12 0307 Flexbox 2
        01:14:57 0307 Flexbox 3
        01:19:09 0308 Position 1
        01:26:02 0308 Position 2
        01:32:27 0309 Posicionamento Exercício 1
        01:43:34 0309 Posicionamento Exercício 2
        """,
    video='BAACAgEAAx0CaeV8BAACARlkhSOyxUSq9piTIDv7SufveEUPQAAC-QQAArKXMUROVJQ5z9QtAAEvBA')
    print("Video 4 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
    
        #Block005

        03  CSS Posicionamento
        00:00:00 0309 Posicionamento Exercício 3
        """,
    video='BAACAgEAAx0CaeV8BAACARtkhSQ3_GoD_k5CWnMp4_HOUclk1gAC-gQAArKXMUTeoBtbkfawni8E')
    print("Video 5 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
        #Block006

        04  HTL e Semântica
        00:00:00 0401 Semântica e Acessibilidade
        00:10:12 0402 Pontos de Referência 1
        00:14:51 0402 Pontos de Referência 2
        00:21:45 0402 Pontos de Referência 3
        00:26:11 0403 Listas
        00:32:03 0404 Navegação
        00:40:31 0405 blockquote, q, cite, em, strong
        """,
    video='BAACAgEAAx0CaeV8BAACAR1khSTenG2SB4-KaQdUaJssrdq5eQAC_QQAArKXMUT72sJkF9C4nC8E')
    print("Video 6 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
            
        #Block007

        05  CSS Propriedades
        00:00:00 0501 Unidades 1
        00:08:39 0501 Unidades 2
        00:16:04 0502 Tipografia
        00:27:47 0503 Background 1
        00:36:46 0503 Background 2
        00:41:54 0504 Pseudo Classes 1
        00:47:45 0504 Pseudo Classes 2
        00:53:36 0505 Pseudo Elements
        01:01:56 0506 Refatorar Exercício 1
        01:08:36 0506 Refatorar Exercício 2
        01:13:40 0506 Refatorar Exercício 3
        """,
    video='BAACAgEAAx0CaeV8BAACAUhkh5nTErnOC5bHZy4m0LtvWw6ItgAC3wMAAqohQUS1NeOJavfoCi8E')
    print("Video 7 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption="""
     
        #Block008

        06  Responsivo
        00:00:00 0601 Responsivo
        00:08:48 0602 Media Queries
        00:18:57 0603 Grid
        00:25:28 0604 Object Fit
        00:28:54 0605 Max Width
        00:33:42 0606 Responsivo Exercicio
        """,
    video='BAACAgEAAx0CaeV8BAACAUpkh5rx2fsbnTpWFKEOsYP0jEoKywAC4AMAAqohQURlv_wqxLB4jC8E')
    print("Video 8 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
            
        #Block009

        07  Projeto Portifólio
        00:00:00 0701 Primeiros Passos
        00:05:25 0702 Design e Código
        00:09:31 0703 Estilos Iniciais
        00:16:50 0704 Header
        00:24:39 0705 Introdução
        00:37:22 0706 Experiência HTML
        00:45:14 0707 Experiência CSS 1
        01:00:09 0707 Experiência CSS 2
        01:05:27 0708 Formação HTML
        01:12:38 0709 Formação CSS 1
        01:23:59 0709 Formação CSS 2
        01:32:42 0710 Footer
        01:39:47 0711 Otimizações
        """,
    video='BAACAgEAAx0CaeV8BAACAUxkh5wvnBUQJzZ3BOZe-T2D_EKMAQAC4QMAAqohQUT-dYVca-vVNi8E')
    print("Video 9 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
    
        #Block010

        08  Ferramentas
        00:00:00 0801-instalar-ferramentas
        00:05:11 0802-linha-de-comando
        00:12:15 0803-npm-e-cleancss
        00:26:36 0804-git 1
        00:33:50 0804-git 2
        00:41:52 0805-fonts
        """,
    video='BAACAgEAAx0CaeV8BAACAU5kh5ysT6JksYYIvvnhn0xXIYeziQAC4gMAAqohQUSJDkKAGBMWIi8E')
    print("Video 10 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
            
        #Block011

        09  ais HTL e CSS
        00:00:00 0901 Formulários 1
        00:10:45 0901 Formulários 2
        00:18:41 0901 Formulários 3
        00:26:35 0901 Formulários 4
        00:32:46 0902 Outros Seletores
        00:41:53 0903 Especificidade
        00:49:41 0904 Propriedades Customizadas
        00:59:51 0905 Modo Claro e Escuro
        01:13:08 0906 CSS Utilitário 1
        01:23:48 0906 CSS Utilitário 2
        """,
    video='BAACAgEAAx0CaeV8BAACAV9kiQNm5aeISPMNso-LbY4ggO29LQAC6QIAAqjLSEQGJRYDlcEkjy8E')
    print("Video 11 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
            
        #Block012

        10  Projeto Final
        00:00:00 1001 Análise Projeto
        00:04:42 1002 Estrutura Inicial
        00:07:41 1003 Repositório Git
        00:10:44 1004 Header e Menu 1
        00:20:34 1004 Header e Menu 2
        00:30:14 1005 Introdução 1
        00:41:20 1005 Introdução 2
        00:48:08 1006 Box Shadow
        00:55:42 1007 Introdução Responsiva
        01:00:00 1008 Tipografia
        01:06:17 1009 Import CSS
        01:12:49 1010 CSS Utilitário
        01:27:52 1011 Tipografia Utilitária 1
        01:36:50 1011 Tipografia Utilitária 2
        01:40:17 1012 Bicicletas Lista 1
        01:53:22 1012 Bicicletas Lista 2
        """,
    video='BAACAgEAAx0CaeV8BAACAWFkiQVLsztuPJNFtFM6401QYxdP9wAC6gIAAqjLSES9RXiS-yIuhS8E')
    print("Video 12 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
    
        #Block013

        10  Projeto Final
        00:00:00 1013 Container
        00:01:58 1014 Tecnologia 1
        00:11:42 1014 Tecnologia 2
        00:21:40 1015 Parceiros
        00:31:08 1016 Depoimento
        00:43:58 1017 Seguros
        00:58:07 1018 Footer
        01:10:57 1019 Termos
        01:20:14 1020 Bicicletas 1
        01:27:13 1020 Bicicletas 2
        01:39:47 1020 Bicicletas 3
        """,
    video='BAACAgEAAx0CaeV8BAACAWNkiQa3zB9nFpcGniwn1TG5AsZI0gAC6wIAAqjLSESBJhMvC2r60C8E')
    print("Video 13 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
    
        #Block014

        10  Projeto Final
        00:00:00 1021 Seguros 1
        00:12:30 1021 Seguros 2
        00:22:21 1022 Bicicleta Interna 1
        00:33:58 1022 Bicicleta Interna 2
        00:46:26 1023 Bicicleta Outras
        00:48:58 1024 Bicicleta Seguro
        00:59:40 1025 Contato Dados 1
        01:09:03 1025 Contato Dados 2
        01:20:39 1026 Contato Formulário
        01:28:53 1027 Contato Lojas
        01:39:09 1028 Orçamento 1
        01:53:04 1028 Orçamento 2
        """,
    video='BAACAgEAAx0CaeV8BAACAWVkiQgGk9M54eYgmPpR9lNq38uXaAAC7AIAAqjLSERcIxSz6pMXuC8E')
    print("Video 14 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
        #Block015

        10  Projeto Final
        00:00:00 1028 Orçamento 3
        00:11:27 1028 Orçamento 4
        00:16:46 1028 Orçamento 5
        00:25:16 1029 Decoração
        00:34:07 1030 Otimizações
        """,
    video='BAACAgEAAx0CaeV8BAACAWdkiQjHZxkd77XqozbdSfLpYVYItgAC7QIAAqjLSES2-eFdGxZnaS8E')
    print("Video 15 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
            
        #Block016

        11  JavaScript Básico
        00:00:00 1101 JavaScript
        00:07:23 1102 Manipular DOM
        00:16:05 1103 Tipos de Dados
        00:21:47 1104 Objetos
        00:35:05 1105 Funções 1
        00:44:46 1105 Funções 2
        00:54:11 1106 Eventos 1
        01:04:45 1106 Eventos 2
        01:15:01 1106 Eventos 3
        01:21:41 1107 Condicionais 1
        01:32:58 1107 Condicionais 2
        01:40:29 1108 Arrays e Loops 1
        """,
    video='BAACAgEAAx0CaeV8BAACAWlkiQmh9IC5yFfE08j3eGLU39fITgAC7gIAAqjLSES__ec3yzKc2S8E')
    print("Video 16 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
        #Block017

        11  JavaScript Básico
        00:00:00 1108 Arrays e Loops 2
        00:10:43 1108 Arrays e Loops 3
        00:16:02 1109 Solucionar Problemas
        """,
    video='BAACAgEAAx0CaeV8BAACAWtkiQnv0c6_ixe98QX6vDcarMJ4AgAC7wIAAqjLSESDs0ieljQYxS8E')
    print("Video 17 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
    
        #Block018

        12  JavaScript Projeto
        00:00:00 1201 Menu Ativo
        00:09:31 1202 Parâmetros URL
        00:21:07 1203 Perguntas Frequentes
        00:35:02 1204 Galeria Imagens
        00:43:02 1205 Plugin Animar
        00:57:05 1206 Plugin Externo
        01:04:54 1207 JavaScript Desativado

        """,
    video='BAACAgEAAx0CaeV8BAACAW1kiQtRdkRzzHPdlXLdS_18okCGGQAC8AIAAqjLSER6yok3S-wHmy8E')
    print("Video 18 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
            
        #Block019

        13  Produção
        00:00:00 1301 Otimizar Produção
        00:06:52 1302 Hospedagem 1
        00:11:57 1302 Hospedagem 2
        00:24:57 1303 Acessar Servidor
        00:30:55 1304 Formulário PHP
        00:52:17 1305 Formulário JavaScript
        """,
    video='BAACAgEAAx0CaeV8BAACAW9kiQyTus9P4rD1VAABDOs0mO_N9U8AAvECAAKoy0hEKjGDaXA8CBQvBA')
    print("Video 19 - Ok")
    print("-----------------------------------------------------------------")

    await update.message.reply_video(caption=""" 
            
        #Block020

        14  Considerações Finais
        00:00:00 1401 HTML e CSS para Iniciantes Conclusão
        """,
    video='BAACAgEAAx0CaeV8BAACAXFkiQzNeqKKR9l3XKF_Hktc21z3LwAC8gIAAqjLSESALmE3fSfSwC8E')
    print("Video 20 - Ok")
    print("-----------------------------------------------------------------")

