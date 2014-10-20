# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'frogPondLog'
        db.create_table(u'reese_frogpondlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, db_index=True)),
            ('data', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'reese', ['frogPondLog'])


    def backwards(self, orm):
        # Deleting model 'frogPondLog'
        db.delete_table(u'reese_frogpondlog')


    models = {
        u'reese.frogpondlog': {
            'Meta': {'object_name': 'frogPondLog'},
            'data': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['reese']