import datetime
from uuid import uuid4

from django.db import models


class Participant(models.Model):
    """ Участник проекта """

    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    first_name = models.CharField(verbose_name='имя', max_length=64)
    last_name = models.CharField(verbose_name='фамилия', max_length=64)
    birthday = models.DateField(verbose_name='дата рождения', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)
    is_activate = models.BooleanField(verbose_name='активная запись', default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # TODO Необходимо реализовать переопределение метода delete не удаляя запись а измененя is_activate
