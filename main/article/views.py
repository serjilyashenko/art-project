from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from main.article.models import Article


def show(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'show.html', locals())
