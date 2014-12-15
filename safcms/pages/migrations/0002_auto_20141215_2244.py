# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='is_active',
            field=models.BooleanField(default=True, help_text="If menu item is active it's visible in menu", verbose_name='is active?'),
            preserve_default=True,
        ),
    ]
