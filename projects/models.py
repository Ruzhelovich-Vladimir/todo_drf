from uuid import uuid4

from django.db import models
from participants.models import Participant


class Project(models.Model):
    """ Проекты """
    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    name = models.CharField(verbose_name='имя', max_length=64)
    repository_url = models.URLField(verbose_name='репозиторий', blank=True)
    project_manager = models.ForeignKey(Participant,
                                       verbose_name='менеджер проекта',
                                       on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(verbose_name='создано',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)
    is_activate = models.BooleanField(verbose_name='активная запись', default=True)

    def __str__(self):
        return f'{self.name}'


class Development(models.Model):
    """ Разработчики """

    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    project = models.ForeignKey(Project,
                               verbose_name='проект',
                               on_delete=models.DO_NOTHING)
    development = models.ForeignKey(Participant,
                                verbose_name='разработчик',
                                on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(verbose_name='создано',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)
    is_activate = models.BooleanField(verbose_name='активная запись', default=True)
