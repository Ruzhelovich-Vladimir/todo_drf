from uuid import uuid4

from django.db import models

from participants.models import Participant
from projects.models import Project


class Note(models.Model):
    """ Заметки """
    STATUS = [
        ('N', 'Новый'),
        ('P', 'В процессе'),
        ('S', 'Отложен'),
        ('D', 'Выполнено')
    ]

    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    project = models.ForeignKey(Project,
                                verbose_name='проект',
                                on_delete=models.DO_NOTHING)
    text = models.TextField(verbose_name='заметка',  max_length=1000)
    author = models.ForeignKey(Participant, verbose_name='Автор', on_delete=models.DO_NOTHING)
    status = models.CharField(choices=STATUS, max_length=1)
    created_at = models.DateTimeField(verbose_name='создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)
    is_activate = models.BooleanField(verbose_name='активная запись', default=True)

    # TODO Необходимо реализовать переопределение метода delete не удаляя запись а измененя is_activate
