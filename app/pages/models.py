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


class MenuItem(NameAbstract):
    parent = models.ForeignKey(
        'self', related_name='childs', blank=True, null=True,
        help_text='If manu item has no parent it is main (index) menu item')

    is_active = models.BooleanField(
        verbose_name='is active?',
        help_text='If menu item is active it\'s visible in menu')

    def clean(self):
        index_exists = MenuItem.objects.filter(parent__isnull=True).exists()
        if not self.parent and index_exists:
            raise ValidationError(
                'Main menu item (without parents) already exists.')


class Page(NameAbstract, SlugAbstract):
    menu_item = models.OneToOneField(
        'MenuItem', related_name='article', blank=True, null=True)
    images = models.ManyToManyField(
        'Image', related_name='articles', blank=True, null=True)
    content = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    @classmethod
    def get_index(cls):
        return cls.objects.get(menu_item__parent__isnull=True).page
