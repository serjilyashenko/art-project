from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^article$', views.show, name='main_article_show'),
]
