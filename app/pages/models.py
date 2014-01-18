from os.path import join
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

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
    parent = models.ForeignKey(
        'self', related_name='childs', blank=True, null=True)
    images = models.ManyToManyField(
        'Image', related_name='articles', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='is active?')
    is_in_menu = models.BooleanField(verbose_name='is in menu?')
    is_index = models.BooleanField(verbose_name='is main page?')
    content = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    def save(self, *args, **kwargs):
        # only one page can be main page
        if self.is_index:
            Page.objects.filter(is_index=True).update(is_index=False)
        return super(Page, self).save(*args, **kwargs)

    def clean(self):
        if not (self.is_index or self.parent):
            raise ValidationError('Only main page can have no parent.')
        if self.is_index and self.parent:
            raise ValidationError('Main page can not have parents.')
