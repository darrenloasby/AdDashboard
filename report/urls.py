from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/$', views.select, name='select'),
    url(r'^view/(?P<gcampaign_id>[0-9]+)/(?P<fbacc_id>[0-9]+)/', views.select_adgroup, name='select_adgroup'),
    #url(r'^(?P<campaign_id>[0-9]+)', views.result, name='result'),
    #url(r'^generate/(?P<time_id>[0-9]+)/$', views.main, name='main'),
    url(r'^generate/(?P<start_date>[-A-Za-z0-9_]+)/(?P<end_date>[-A-Za-z0-9_]+)/', views.collect, name='collect'),
    #url(r'^view/$', views.select, name = 'select'),
    #url(r'^campaigns/', views.campaigns, name='campaigns'),
    #url(r'^adgroups/(?P<adgroup_id>[0-9]+)', views.adgroup, name = 'adgroup'),
    #url(r'^login/', views.login, name = 'login'),
    ]

