# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20141215_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='content_type',
            field=models.IntegerField(default=1, choices=[(1, 'markdown'), (2, 'html'), (3, 'markdown from url')], verbose_name='content type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='content_type',
            field=models.IntegerField(default=1, choices=[(1, 'markdown'), (2, 'html'), (3, 'markdown from url')], verbose_name='content type'),
            preserve_default=True,
        ),
    ]
