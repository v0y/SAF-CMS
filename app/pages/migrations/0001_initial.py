# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Box'
        db.create_table('pages_box', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='boxes', to=orm['pages.Page'])),
            ('codename', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('pages', ['Box'])

        # Adding model 'Image'
        db.create_table('pages_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['pages.Page'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('pages', ['Image'])

        # Adding model 'MenuItem'
        db.create_table('pages_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, blank=True, max_length=64)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', to=orm['pages.MenuItem'], null=True, blank=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, related_name='menu_item', to=orm['pages.Page'], null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('pages', ['MenuItem'])

        # Adding model 'Page'
        db.create_table('pages_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, blank=True, null=True)),
            ('short', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('pages', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Box'
        db.delete_table('pages_box')

        # Deleting model 'Image'
        db.delete_table('pages_image')

        # Deleting model 'MenuItem'
        db.delete_table('pages_menuitem')

        # Deleting model 'Page'
        db.delete_table('pages_page')


    models = {
        'pages.box': {
            'Meta': {'object_name': 'Box'},
            'Page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boxes'", 'to': "orm['pages.Page']"}),
            'codename': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pages.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['pages.Page']", 'null': 'True', 'blank': 'True'})
        },
        'pages.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'blank': 'True', 'max_length': '64'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'related_name': "'menu_item'", 'to': "orm['pages.Page']", 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': "orm['pages.MenuItem']", 'null': 'True', 'blank': 'True'})
        },
        'pages.page': {
            'Meta': {'object_name': 'Page', 'ordering': "['name']"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'short': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['pages']