# Generated by Django 4.1.7 on 2023-02-25 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name="Ім'я")),
                ('second_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прізвище')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Електрона пошта')),
                ('phone_number', models.CharField(blank=True, max_length=13, verbose_name='Номер телефона')),
                ('chat_id', models.CharField(blank=True, max_length=100, verbose_name='Індетифікатор чата')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Створено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Видалено')),
            ],
            options={
                'verbose_name': 'Користувач',
                'verbose_name_plural': 'Користувачі',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('chat_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webhook.chatuser')),
            ],
        ),
    ]
