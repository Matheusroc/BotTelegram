import asyncio
import telegram
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def utils(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(parse_mode="HTML",
        chat_id=update.effective_chat.id,
        text="""utils:
            Chat-GPT | https://chat.openai.com
            BingChat | https://www.microsoft.com/pt-br/bing
            Claude-instant | https://www.anthropic.com
            Poe | https://poe.com
            ManyChat | https://manychat.com
            Nomes para Negócios |  https://namelix.com
            Criação de Logos |  https://looka.com
            Comprar Domínios |  https://namecheap.com
            Gerar Ideias |  https://chat.openai.com   
            Escrita |  https://grammarly.com 
            Copywriting |  https://copy.ai 
            Pesquisa |  https://answerthepublic.com    
            Produtividade |  https://notion.so   
            Criar páginas |  https://typedream.com 
            Site Analytics |  https://usefathom.com 
            Criar Apps |  https://bubble.io
            SEO |  https://semrush.com
            Twitter |  https://typefully.com
            Linkedin |  https://taplio.com
            Youtube |  https://tubebuddy.com
            Newsletter |  https://beehiiv.com 
            Comunidades |  https://circle.so
            Depoimentos |  https://senja.io
            Mensagem de Vídeo |  https://loom.com 
            E-mails |  https://mailchimp.com
            Comparar preços |  https://zoom.com.br 
            Pagamentos |  https://stripe.com
            Vender Produtos |  https://gumroad.com
            Link na bio |  https://zaap.ai
            Protótipos |  https://figma.com 
            Design |  https://canva.com
            Ilustrações |  https://drawkit.com 
            Ícones |  https://iconscout.com
            Banco de Conteúdos |  https://pixabay.com
            Animações |  https://jitter.video
            Apresentações |  https://tome.app
            Automação |  https://zapier.com
            Editor de Vídeo |  https://capcut.com 
            Produtos |  https://producthunt.com 
            Marketplace |  https://appsumo.com 
            Marketing | https://arketingexamples.com
            Clonar voz | https://beta.elevenlabs.io
        """
    )