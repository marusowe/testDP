# Generated by Django 3.2.3 on 2021-05-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort_api', '0003_remove_urlshort_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshort',
            name='user_session_key',
            field=models.CharField(default='123123fdsfsd23', max_length=50, verbose_name='Ключ сессии пользователя'),
            preserve_default=False,
        ),
    ]