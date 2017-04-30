from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models.aggregates import Count
from main.section.models import Section


def home(request):
    sections = Section.objects.filter(parent=None)\
        .annotate(children_count=Count('children'))\
        .prefetch_related('articles')\
        .order_by('id')

    return render(request, 'home.html', locals())
