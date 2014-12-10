from django.conf.urls import patterns, include, url
from authentication.urls import url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
