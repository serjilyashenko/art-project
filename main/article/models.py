# ~*~ coding: utf-8 ~*~
from django.db import models
from general.models import AppModel


class Article(AppModel):
    title = models.CharField("Заголовок", max_length=255, blank=True)
    text = models.TextField("Содержание", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        db_table = 'site_article'
