from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import Template, RequestContext
from main.article.models import Article


def show(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    section = article.section

    article_text_template = Template(article.text)
    article.text = article_text_template.render(RequestContext(request, locals()))

    return render(request, 'show.html', locals())
