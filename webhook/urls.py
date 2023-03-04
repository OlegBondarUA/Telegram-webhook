from django.urls import path
from decouple import config
from . import views

TOKEN = config('TELEGRAM_TOKEN')

urlpatterns = [
    path('webhook/', views.telegram_webhook, name='webhook'),
]
