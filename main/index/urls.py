from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.home, name='main_index_home'),
    url(r'^sitemap$', views.sitemap, name='main_index_sitemap'),
    url(r'^contacts$', views.contacts, name='main_index_contacts'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]
