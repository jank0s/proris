from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('webapp.urls')),
    url(r'^admin/mypage/$', 'webapp.views.importcsv'),
    url(r'^admin/', include(admin.site.urls)),
)
