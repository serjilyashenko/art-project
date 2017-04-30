# ~*~ coding: utf-8 ~*~
from django.db import models
from general.models import AppModel


class Section(AppModel):
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL, related_name="children",
                               verbose_name="Родительский раздел")
    title = models.CharField("Заголовок", max_length=255, blank=True)
    photo = models.TextField("Картинка", max_length=500, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        db_table = 'site_section'
