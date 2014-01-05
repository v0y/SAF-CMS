from django.db import models

from app.shared.models import NameAbstract, SlugAbstract


class Page(NameAbstract, SlugAbstract):
    is_active = models.BooleanField(verbose_name='is active?')
    content = models.TextField()
    image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['name']
        verbose_name = 'page'
        verbose_name_plural = 'pages'
