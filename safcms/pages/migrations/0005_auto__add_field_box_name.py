# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Box.name'
        db.add_column('pages_box', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=128, default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Box.name'
        db.delete_column('pages_box', 'name')


    models = {
        'pages.box': {
            'Meta': {'object_name': 'Box'},
            'codename': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['pages.Page']", 'related_name': "'boxes'"})
        },
        'pages.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['pages.Page']", 'related_name': "'images'"})
        },
        'pages.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True', 'unique': 'True'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'blank': 'True', 'null': 'True', 'to': "orm['pages.Page']", 'related_name': "'menu_item'"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['pages.MenuItem']", 'related_name': "'children'"})
        },
        'pages.page': {
            'Meta': {'ordering': "['name']", 'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True'}),
            'short': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['pages']