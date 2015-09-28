from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', name='site_login'),
    url(r'^accounts/logout/$', 'login', name='site_logout'),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tenders/$', 'procurement.views.tenders', name='tender_list'),
    url(r'^upload/(?P<id>\d+)/$', 'procurement.views.upload', name='uploads'),
    url(
        r'^download/(?P<id>\d+)/$',
        'procurement.views.download',
        name='download'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.contrib.staticfiles.views',
        (r'^static/(?P<path>.*)$', 'serve'),
    )
