# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UploadedDoc.upload'
        db.add_column(u'procurement_uploadeddoc', 'upload',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UploadedDoc.upload'
        db.delete_column(u'procurement_uploadeddoc', 'upload')


    models = {
        u'procurement.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'procurement.criteria': {
            'Meta': {'object_name': 'Criteria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'procurement.documentation': {
            'Meta': {'object_name': 'Documentation'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'procurement.rating': {
            'Meta': {'object_name': 'Rating'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procurement.Company']"}),
            'criterion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procurement.Criteria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procurement.Tender']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'procurement.result': {
            'Meta': {'object_name': 'Result'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procurement.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procurement.Tender']"}),
            'value': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'procurement.tender': {
            'Meta': {'object_name': 'Tender'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'procurement.uploadeddoc': {
            'Meta': {'object_name': 'UploadedDoc'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procurement.Company']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procurement.Documentation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procurement.Tender']"}),
            'upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'upload_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'})
        }
    }

    complete_apps = ['procurement']