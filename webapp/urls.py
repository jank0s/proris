from django.conf.urls import patterns, url

from webapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),

                       url(r'^year/$', views.year, name='year'),
                       url(r'^pb/(?P<year>\d+)/$', views.pb, name='pb'),
                       url(r'^pb/(?P<year>\d+)/(?P<pb_id>\d+)/$', views.pb_item, name='pb_item'),
                       url(r'^bug/(?P<year>\d+)/$', views.bug, name='bug'),
                       url(r'^bug/(?P<year>\d+)/(?P<bug_id>\d+)/$', views.bug_bu, name='bug_bu'),
                       url(r'^bug/(?P<year>\d+)/(?P<bug_id>\d+)/(?P<bu_id>\d+)/$', views.bug_bu_item, name='bug_bu_item'),
)
