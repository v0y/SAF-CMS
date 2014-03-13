# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Box', fields ['codename']
        db.create_unique('pages_box', ['codename'])


    def backwards(self, orm):
        # Removing unique constraint on 'Box', fields ['codename']
        db.delete_unique('pages_box', ['codename'])


    models = {
        'pages.box': {
            'Meta': {'object_name': 'Box'},
            'Page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']", 'related_name': "'boxes'"}),
            'codename': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pages.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['pages.Page']", 'blank': 'True', 'related_name': "'images'"})
        },
        'pages.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'to': "orm['pages.Page']", 'unique': 'True', 'blank': 'True', 'related_name': "'menu_item'"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['pages.MenuItem']", 'blank': 'True', 'related_name': "'children'"})
        },
        'pages.page': {
            'Meta': {'ordering': "['name']", 'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True'}),
            'short': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'unique': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']