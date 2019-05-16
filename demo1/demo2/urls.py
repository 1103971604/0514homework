from django.conf.urls import url
from . import views

app_name='demo2url'

urlpatterns = [
    url(r'^dem123123o2list/$', views.list,name='list'),
    url(r'^dem213123o2hero/(\d+)/$', views.hero,name='hero'),
    url(r'^index/$',views.index,name='index')
]









