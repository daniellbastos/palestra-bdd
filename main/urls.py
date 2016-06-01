from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('clients.urls', namespace='clients')),
    url(r'^admin/', include(admin.site.urls)),
]
