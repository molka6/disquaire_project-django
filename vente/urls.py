from django.conf.urls import url

from . import views 


urlpatterns = [

url(r'index', views.index),
url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
 url(r'^search/$', views.search, name='search'),


]