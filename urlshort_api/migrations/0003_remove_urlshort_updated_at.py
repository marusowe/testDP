# Generated by Django 3.2.3 on 2021-05-16 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort_api', '0002_alter_urlshort_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshort',
            name='updated_at',
        ),
    ]