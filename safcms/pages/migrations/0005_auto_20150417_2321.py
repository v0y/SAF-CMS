# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_menuitem_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['position', 'name']},
        ),
        migrations.AddField(
            model_name='menuitem',
            name='position',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
