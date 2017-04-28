from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^articles/([0-9]+)$', views.show, name='main_article_show'),
]
