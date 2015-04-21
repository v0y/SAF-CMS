# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150417_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_title',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
