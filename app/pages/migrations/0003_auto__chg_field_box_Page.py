# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Box.Page'
        db.alter_column('pages_box', 'Page_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['pages.Page']))

    def backwards(self, orm):

        # Changing field 'Box.Page'
        db.alter_column('pages_box', 'Page_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Page'], default=None))

    models = {
        'pages.box': {
            'Meta': {'object_name': 'Box'},
            'Page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boxes'", 'null': 'True', 'to': "orm['pages.Page']", 'blank': 'True'}),
            'codename': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pages.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'null': 'True', 'to': "orm['pages.Page']", 'blank': 'True'})
        },
        'pages.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'blank': 'True', 'max_length': '64'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'menu_item'", 'null': 'True', 'to': "orm['pages.Page']", 'unique': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'null': 'True', 'to': "orm['pages.MenuItem']", 'blank': 'True'})
        },
        'pages.page': {
            'Meta': {'object_name': 'Page', 'ordering': "['name']"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'short': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'null': 'True', 'blank': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['pages']