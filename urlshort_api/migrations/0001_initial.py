# Generated by Django 3.2.3 on 2021-05-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.URLField(unique=True, verbose_name='Ссылка')),
                ('hash', models.CharField(max_length=10, unique=True, verbose_name='Хэш ссылки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Сокращенная ссылка',
                'verbose_name_plural': 'Сокращенные ссылки',
            },
        ),
    ]