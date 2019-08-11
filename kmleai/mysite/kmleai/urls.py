"""kmleai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
#from django.contrib.staticfiles import views
from django.contrib import admin
from indextensorflow.views import index
from django.conf.urls import (
 handler400, handler403, handler404, handler500
)

handler400 = 'indextensorflow.views.test'
handler403 = 'indextensorflow.views.test'
handler404 = 'indextensorflow.views.test'
handler500 = 'indextensorflow.views.test'

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^examination/', include('examination.urls', namespace='examination')),
    url(r'^quiz/', include('quiz.urls', namespace='quiz')),
    url(r'^information/', include('information.urls', namespace='information')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^halloffame/', include('halloffame.urls')),
#    url(r'^static/(?P.+)', views.serve),
#    url(r'^media/(?P.+)', views.serve, kwargs={'insecure': True}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,insecure=True)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,insecure=True)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
