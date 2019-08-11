from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.examination_form, name='examination_form'),
    url(r'^(?P<pk>\d+)/$', views.examination_detail, name='examination_detail'),
]



