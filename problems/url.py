from django.conf.urls import url, include

from problems import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^index1/', views.index1, name='index1'),
]