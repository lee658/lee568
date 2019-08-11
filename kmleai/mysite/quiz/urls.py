from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.quiz_list, name='quiz_list'),
    url(r'^(?P<pk>\d+)/$', views.quiz_detail, name='quiz_detail'),
    url(r'^newQuiz/$', views.quiz_new, name='quiz_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.quiz_edit, name='quiz_edit'),
]
 
