from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new-today/$', views.new_computers_today, name='new_computers_today'),
    url(r'^in-progress/$', views.in_progress, name='in_progress'),
    url(r'^error/$', views.error, name='error'),
    url(r'^completed/$', views.completed, name='completed'),
    url(r'^info/(?P<computer_serial>.+)/', views.info, name='info'),
    url(r'^$', views.index, name='index'),
]
