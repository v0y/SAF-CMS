# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150131_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(null=True, unique=True, blank=True),
            preserve_default=True,
        ),
    ]
