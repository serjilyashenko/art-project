from __future__ import unicode_literals

from django.shortcuts import render
from main.section.models import Section


def home(request):
    sections_list = Section.objects.filter(type=1).order_by('id').all()

    return render(request, 'home.html', locals())
