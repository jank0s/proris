from django.conf.urls import patterns, url

from webapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^pb/(?P<year>\d+)/$', views.pb, name='pb'),
)