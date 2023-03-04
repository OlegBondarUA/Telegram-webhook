import datetime

from django.db import models


class ChatUser(models.Model):
    chat_id = models.IntegerField()
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Message(models.Model):
    chat_user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    message = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class User(models.Model):
    class Role(models.TextChoices):
        CLIENT = 'CLIENT', 'Client'
        PARTNER = 'PARTNER', 'Partner'
        DRIVER = 'DRIVER', 'Driver'
        DRIVER_MANAGER = 'DRIVER_MANAGER', 'Driver manager'
        SERVICE_STATION_MANAGER = 'SERVICE_STATION_MANAGER', 'Service station manager'
        SUPPORT_MANAGER = 'SUPPORT_MANAGER', 'Support manager'
        OWNER = 'OWNER', 'Owner'

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ім'я")
    second_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Прізвище')
    email = models.EmailField(blank=True, max_length=254, verbose_name='Електрона пошта')
    phone_number = models.CharField(blank=True, max_length=13, verbose_name='Номер телефона')
    chat_id = models.CharField(blank=True, max_length=100, verbose_name='Індетифікатор чата')
    created_at = models.DateTimeField(editable=False, auto_now=datetime.datetime.now(), verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Видалено')

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self)-> str:
        return self.full_name()

    def full_name(self):
        return f'{self.name} {self.second_name}'

    @staticmethod
    def get_by_chat_id(chat_id):
        """
        Returns user by chat_id
        :param chat_id: chat_id by which we need to find the user
        :type chat_id: str
        :return: user object or None if a user with such ID does not exist
        """
        try:
            user = User.objects.get(chat_id=chat_id)
            return user
        except User.DoesNotExist:
            return None
