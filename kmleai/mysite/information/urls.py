from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.information_list, name='information_list'),
    url(r'^(?P<pk>\d+)/$', views.information_detail, name='information_detail'),
    url(r'^newInformation/$', views.information_new, name='information_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.information_edit, name='information_edit'),
]
