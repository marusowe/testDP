from django.db import models
from hashlib import md5
from config import settings
import secrets


class UrlShort(models.Model):
    full_url = models.URLField(verbose_name='Ссылка')
    hash = models.CharField(max_length=128, unique=True, verbose_name='Хэш ссылки')
    user_session_key = models.CharField(max_length=70, verbose_name='Ключ сессии пользователя')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Сокращенная ссылка'
        verbose_name_plural = 'Сокращенные ссылки'

    def __str__(self):
        return f'Короткая ссылка {self.full_url} для {self.hash}'

    @staticmethod
    def _generate_hash(len_hash):
        return secrets.token_urlsafe(len_hash)

    @classmethod
    def _hash_exists(cls, url_hash):
        return cls.objects.filter(hash=url_hash).exists()

    def save(self, *args, **kwargs):
        if self._state.adding and not self.hash:
            url_hash = self._generate_hash(settings.HASH_LENGTH)
            while self._hash_exists(url_hash):
                url_hash = self._generate_hash(settings.HASH_LENGTH)
            self.hash = url_hash
        super().save(*args, **kwargs)

    @property
    def short_url(self):
        return f'{settings.PROTOCOL}://{settings.DOMAIN_NAME}/{self.hash}/'

