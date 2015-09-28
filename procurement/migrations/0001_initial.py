# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'procurement_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'procurement', ['Company'])

        # Adding model 'Tender'
        db.create_table(u'procurement_tender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'procurement', ['Tender'])

        # Adding model 'Documentation'
        db.create_table(u'procurement_documentation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'procurement', ['Documentation'])

        # Adding model 'UploadedDoc'
        db.create_table(u'procurement_uploadeddoc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procurement.Tender'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procurement.Company'])),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procurement.Documentation'])),
            ('upload_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
        ))
        db.send_create_signal(u'procurement', ['UploadedDoc'])

        # Adding model 'Criteria'
        db.create_table(u'procurement_criteria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'procurement', ['Criteria'])

        # Adding model 'Rating'
        db.create_table(u'procurement_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procurement.Company'])),
            ('criterion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procurement.Criteria'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'procurement', ['Rating'])

        # Adding model 'Result'
        db.create_table(u'procurement_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procurement.Company'])),
            ('tender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procurement.Tender'])),
            ('value', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'procurement', ['Result'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'procurement_company')

        # Deleting model 'Tender'
        db.delete_table(u'procurement_tender')

        # Deleting model 'Documentation'
        db.delete_table(u'procurement_documentation')

        # Deleting model 'UploadedDoc'
        db.delete_table(u'procurement_uploadeddoc')

        # Deleting model 'Criteria'
        db.delete_table(u'procurement_criteria')

        # Deleting model 'Rating'
        db.delete_table(u'procurement_rating')

        # Deleting model 'Result'
        db.delete_table(u'procurement_result')


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
            'upload_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'})
        }
    }

    complete_apps = ['procurement']