__author__ = 'ranveer'
from django.conf.urls import patterns, include, url
from authentication import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^register/', views.register, name='register'),
    #url(r'^login', views.authentication, name='login'),
    #url(r'^logout', views.logout, name='logout'),
)
