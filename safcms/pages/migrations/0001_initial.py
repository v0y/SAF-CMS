# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import safcms.pages.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128, blank=True)),
                ('codename', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('content_type', models.IntegerField(choices=[(1, 'markdown'), (2, 'html')], verbose_name='content type', default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=256, blank=True, null=True)),
                ('image', models.ImageField(upload_to=safcms.pages.models.Image.rename_image)),
            ],
            options={
                'verbose_name_plural': 'images',
                'verbose_name': 'image',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64, blank=True, unique=True)),
                ('is_active', models.BooleanField(verbose_name='is active?', help_text="If menu item is active it's visible in menu")),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True, null=True)),
                ('short', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('content_type', models.IntegerField(choices=[(1, 'markdown'), (2, 'html')], verbose_name='content type', default=1)),
            ],
            options={
                'verbose_name_plural': 'pages',
                'ordering': ['name'],
                'verbose_name': 'page',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=models.OneToOneField(blank=True, related_name='menu_item', to='pages.Page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, related_name='children', to='pages.MenuItem', help_text='If manu item has no parent it is main (index) menu item', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='page',
            field=models.ForeignKey(blank=True, related_name='images', to='pages.Page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='box',
            name='page',
            field=models.ForeignKey(blank=True, related_name='boxes', to='pages.Page', null=True),
            preserve_default=True,
        ),
    ]
