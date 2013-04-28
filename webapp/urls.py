from django.conf.urls import patterns, include, url

from tastypie.api import Api
from webapp.resources import BalanceResource, GroupResource, BudgerUserGroupResource, BudgetUserResource, PoliticalBranchResource, ProgrammeResource, CategoryResource, ItemResource
from webapp import views

v1_api = Api(api_name='v1')
v1_api.register(BalanceResource())
v1_api.register(GroupResource())
v1_api.register(BudgerUserGroupResource())
v1_api.register(BudgetUserResource())
v1_api.register(PoliticalBranchResource())
v1_api.register(ProgrammeResource())
v1_api.register(CategoryResource())
v1_api.register(ItemResource())

urlpatterns = patterns('',
                       url(r'^api/', include(v1_api.urls)),
                       url(r'^', views.index, name='index'),
                       url(r'^pb/(?P<year>\d+)/$', views.pb, name='pb'),
                       url(r'^pb/(?P<year>\d+)/(?P<pb_id>\d+)/$', views.pb_item, name='pb_item'),
                       url(r'^bug/(?P<year>\d+)/$', views.bug, name='bug'),
                       url(r'^bug/(?P<year>\d+)/(?P<bug_id>\d+)/$', views.bug_bu, name='bug_bu'),
                       url(r'^bug/(?P<year>\d+)/(?P<bug_id>\d+)/(?P<bu_id>\d+)/$', views.bug_bu_item, name='bug_bu_item'),
)