from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.index.urls')),
    url(r'', include('main.article.urls')),
]
