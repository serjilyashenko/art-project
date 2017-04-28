from django.db import models


class AppModel(models.Model):

    class Meta:
        abstract = True

    def save(self):
        return True
