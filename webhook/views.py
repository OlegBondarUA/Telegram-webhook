# У цьому завданні ми будемо зберігати користувачів
# та їх повідомлення в базі даних

# Для цього ми створимо моделі ChatUser та Message
# Імпортуємо бібліотеку telegram, щоб отримати доступ до API
# Імпортуємо бібліотеку decouple, щоб отримати доступ до змінних середовища
# Імпортуємо бібліотеку json, щоб працювати з JSON
# Імпортуємо бібліотеку HttpResponse, щоб відправляти HTTP відповідь
# Імпортуємо бібліотеку csrf_exempt, щоб відключити захист CSRF
# Імпортуємо моделі ChatUser та Message для збереження даних
# Використовую ngrok для того, щоб отримати доступ до веб-сервера з інтернету


import telegram
import json

from decouple import config
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import ChatUser, Message


# ініціалізуємо бота
bot = telegram.Bot(token=config('TELEGRAM_TOKEN'))


# функція, яка буде викликатися при отриманні повідомлення
@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        update = telegram.Update.de_json(json.loads(request.body), bot)
        message = update.message
        chat_id = message.chat_id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        # зберігаємо користувача
        chat_user, created = ChatUser.objects.get_or_create(
            chat_id=chat_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        # зберігаємо повідомлення
        user_message = Message.objects.create(
            chat_user=chat_user,
            message=message.text
        )

        # повертаємо HTTP відповідь
        return HttpResponse('OK')
