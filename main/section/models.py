# ~*~ coding: utf-8 ~*~
from django.db import models
from general.models import AppModel


class Section(AppModel):
    title = models.CharField("Заголовок", max_length=255, blank=True)
    type = models.PositiveSmallIntegerField("Тип")
    photo = models.TextField("Картинка", max_length=500, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        db_table = 'site_section'
