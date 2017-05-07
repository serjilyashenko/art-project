# ~*~ coding: utf-8 ~*~
from django.db import models
from django.core.urlresolvers import reverse
from general.models import AppModel


class Section(AppModel):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='children',
                               verbose_name='Родительский раздел')
    title = models.CharField('Заголовок', max_length=255, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        db_table = 'site_section'

    def get_absolute_url(self):
        if self.articles.first():
            return reverse('main_article_show', args=[str(self.articles.first().id)])
        return ''

    def get_link(self):
        if self.articles.first():
            return u'<a href="%s">%s</a>' % (self.get_absolute_url(), self.title)
        return u'<span>%s</span>' % self.title

    def get_img(self):
        return u'images/sections/section-%s-200x200.jpg' % self.id

    @property
    def parent_sections(self):
        sections = []
        current_section = self.parent
        while current_section is not None:
            sections.append(current_section)
            current_section = current_section.parent
        return reversed(sections)
