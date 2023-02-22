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