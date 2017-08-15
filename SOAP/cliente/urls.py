from django.conf.urls import include,url

from . import views

app_name = 'soap'
urlpatterns = [
    url(r'^$', views.soap, name="soap"),
    url(r'^$', views.soap2, name="soap"),
]
