from django.contrib import admin

from procurement.models import Company, Tender, Documentation, UploadedDoc, \
    Criteria, Rating, Result


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_id', 'address', 'phone', 'email')


class TenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date', 'active')


class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active')


class UploadedDocAdmin(admin.ModelAdmin):
    list_display = ('tender', 'company', 'document', 'upload_date', 'download')
    list_filter = ('document', 'tender')
    search_fields = ('company__name',)


class CriteriaAdmin(admin.ModelAdmin):
    list_display = ('name',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('company', 'criterion', 'tender', 'value')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('company', 'tender', 'value')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Tender, TenderAdmin)
admin.site.register(Documentation, DocumentationAdmin)
admin.site.register(UploadedDoc, UploadedDocAdmin)
admin.site.register(Criteria, CriteriaAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Result, ResultAdmin)
