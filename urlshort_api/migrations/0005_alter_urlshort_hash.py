# Generated by Django 3.2.3 on 2021-05-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort_api', '0004_urlshort_user_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshort',
            name='hash',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Хэш ссылки'),
        ),
    ]