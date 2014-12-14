from django.db import models

from .helpers import slugify


class NameAbstract(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class SlugAbstract(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # create slug
        if not self.slug:
            self.slug = slugify(self.name)

        # run normal save
        return super(SlugAbstract, self).save(*args, **kwargs)
