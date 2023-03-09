import json
import telegram

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters
from decouple import config


TOKEN = config('TELEGRAM_TOKEN')


bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        json_string = request.body.decode('utf-8')
        update = telegram.Update.de_json(json.loads(json_string), bot)
        dp.process_update(update)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


def handle_message(update, context):
    text = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text='You said: ' + text)


dp.add_handler(CommandHandler('start', handle_message))
dp.add_handler(CommandHandler('help', handle_message))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))


if __name__ == '__main__':

    updater.start_webhook(
        listen='0.0.0.0',
        port=80,
        webhook_url=f'{your_domain}/webhook'
    )
    updater.idle()

