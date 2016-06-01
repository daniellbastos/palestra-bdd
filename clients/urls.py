from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    'clients.views',
    url(r'^$', views.ClientListView.as_view(), name='client-list'),
    url(r'^novo/$', views.ClientCreateView.as_view(), name='client-create'),
    url(r'^inativos/$', views.InactiveClientListView.as_view(), name='inactive-client-list'),
)
