from os.path import join
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models

from app.shared.helpers import shorten
from app.shared.models import NameAbstract, SlugAbstract


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

    def __unicode__(self):
        return shorten(self.description, 25) or 'image'


class MenuItem(NameAbstract):
    parent = models.ForeignKey(
        'self', related_name='children', blank=True, null=True,
        help_text='If manu item has no parent it is main (index) menu item')
    page = models.OneToOneField(
        'Page', related_name='menu_item', blank=True, null=True)
    is_active = models.BooleanField(
        verbose_name='is active?',
        help_text='If menu item is active it\'s visible in menu')

    def clean(self):
        existing_index = MenuItem.objects.filter(parent__isnull=True) \
            .only('pk').first()

        if not self.parent and existing_index and self.pk != existing_index.pk:
            raise ValidationError(
                'Main menu item (without parents) already exists.')

    def get_absolute_url(self):
        return reverse('page', args=[self.page.slug]) if self.page else '#'

    @classmethod
    def get_index(cls):
        return cls.objects.get(parent__isnull=True)


class Page(NameAbstract, SlugAbstract):
    content = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    @staticmethod
    def get_index():
        return MenuItem.get_index().page
