from django.urls import path
from . import views

app_name="app"
urlpatterns = [
    path('',views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('serviceDetail', views.serviceDetail, name = 'serviceDetail'),
]