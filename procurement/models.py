from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Company(models.Model):
    name = models.CharField(max_length=100)
    company_id = models.CharField(max_length=10, unique=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __unicode__(self):
        return self.name


class Tender(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


class Documentation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class UploadedDoc(models.Model):
    tender = models.ForeignKey(Tender, related_name='documents')
    company = models.ForeignKey(Company)
    document = models.ForeignKey(Documentation)
    upload = models.FileField(upload_to='uploads')
    upload_date = models.DateField(default=date.today)

    class Meta:
        unique_together = ('tender', 'company', 'document')

    def __unicode__(self):
        return unicode(self.company)

    def download(self):
        link = '<a href="/download/%d/">download</a>' % self.pk
        return mark_safe(link)
    download.allow_tags = True
    download.short_description = 'Download Document'


class Criteria(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Criteria'

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    company = models.ForeignKey(Company)
    criterion = models.ForeignKey(Criteria)
    tender = models.ForeignKey(Tender)
    value = models.IntegerField()

    def __unicode__(self):
        return unicode(self.company)


class Result(models.Model):
    company = models.ForeignKey(Company)
    tender = models.ForeignKey(Tender)
    value = models.PositiveIntegerField()

    def __unicode__(self):
        return unicode(self.company)
