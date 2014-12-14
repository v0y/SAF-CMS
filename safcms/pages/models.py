from os.path import join
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models

from safcms.shared.helpers import shorten
from safcms.shared.models import NameAbstract, SlugAbstract
from .enums import PageContentTypes, CONTENT_TYPE_CHOICES


class Box(models.Model):
    page = models.ForeignKey(
        'Page', related_name='boxes', blank=True, null=True)
    name = models.CharField(blank=True, max_length=128)
    codename = models.SlugField(unique=True)
    content = models.TextField()
    content_type = models.IntegerField(
        choices=CONTENT_TYPE_CHOICES, verbose_name='content type', default=1)

    def __str__(self):
        return self.name or self.codename

    @property
    def is_html(self):
        return self.content_type == PageContentTypes.HTML

    @property
    def is_markdown(self):
        return self.content_type == PageContentTypes.MARKDOWN


class Image(models.Model):
    def rename_image(self, filename, upload_to='images'):
        ext = filename.split('.')[-1]
        new_filename = '%s.%s' % (uuid4(), ext)
        return join(upload_to, new_filename)

    page = models.ForeignKey(
        'Page', related_name='images', blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to=rename_image)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return shorten(self.description, 25) or 'image'


class MenuItem(models.Model):
    name = models.CharField(max_length=64, blank=True, unique=True)
    parent = models.ForeignKey(
        'self', related_name='children', blank=True, null=True,
        help_text='If manu item has no parent it is main (index) menu item')
    page = models.OneToOneField(
        'Page', related_name='menu_item', blank=True, null=True)
    is_active = models.BooleanField(
        verbose_name='is active?',
        help_text='If menu item is active it\'s visible in menu')

    def __str__(self):
        return self.name

    def clean(self):
        existing_index = MenuItem.objects.filter(parent__isnull=True) \
            .only('pk').first()

        if not self.parent and existing_index and self.pk != existing_index.pk:
            raise ValidationError(
                'Main menu item (without parents) already exists.')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.page.name
        return super(MenuItem, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('page', args=[self.page.slug]) if self.page else '#'

    @classmethod
    def get_index(cls):
        return cls.objects.get(parent__isnull=True)


class Page(NameAbstract, SlugAbstract):
    short = models.TextField(blank=True)
    content = models.TextField(blank=True)
    content_type = models.IntegerField(
        choices=CONTENT_TYPE_CHOICES, verbose_name='content type', default=1)

    class Meta:
        ordering = ['name']
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    @staticmethod
    def get_index():
        return MenuItem.get_index().page

    @property
    def is_html(self):
        return self.content_type == PageContentTypes.HTML

    @property
    def is_markdown(self):
        return self.content_type == PageContentTypes.MARKDOWN

