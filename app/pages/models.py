from os.path import join
from uuid import uuid4

from django.db import models
from django.conf import settings

from app.shared.helpers import shorten
from app.shared.models import NameAbstract, SlugAbstract


class Image(models.Model):
    def rename_image(self, filename, upload_to='images'):
        ext = filename.split('.')[-1]
        new_filename = '%s.%s' % (uuid4(), ext)
        return join(upload_to, new_filename)

    description = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to=rename_image)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __unicode__(self):
        return shorten(self.description, 25) or 'image'


class Page(NameAbstract, SlugAbstract):
    is_active = models.BooleanField(verbose_name='is active?')
    content = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'page'
        verbose_name_plural = 'pages'
