from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models.aggregates import Count
from main.section.models import Section


def home(request):
    sections = Section.objects.filter(parent=None)\
        .annotate(children_count=Count('children'))\
        .prefetch_related('articles')\
        .exclude(articles=None)\
        .order_by('id')

    for section in sections:
        section.article = section.articles.first()

    return render(request, 'home.html', locals())


def sitemap(request):
    sections = Section.objects.filter(parent=None) \
        .prefetch_related('articles') \
        .exclude(articles=None) \
        .order_by('id')

    return render(request, 'sitemap.html', locals())


def contacts(request):
    return render(request, 'contacts.html', locals())
