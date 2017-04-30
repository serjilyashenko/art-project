from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='main_index_home'),
    url(r'^sitemap$', views.sitemap, name='main_index_sitemap'),
]
