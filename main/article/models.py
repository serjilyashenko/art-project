# ~*~ coding: utf-8 ~*~
from django.db import models
from general.models import AppModel
from main.section.models import Section


class Article(AppModel):
    section = models.ForeignKey(Section, related_name="articles", null=True, verbose_name="Раздел")
    title = models.CharField("Заголовок", max_length=255, blank=True)
    text = models.TextField("Содержание", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        db_table = 'site_article'
