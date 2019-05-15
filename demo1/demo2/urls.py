from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.list),
    url(r'^hero/(\d+)/$', views.hero),
    url(r'^index/$',views.index)

]









