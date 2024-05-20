from django.urls import path
from . import views
from .views import *


app_name="dashboard"
urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('',views.index, name='index'),

    path('team',views.team, name='team'),
    path('add/hosting',views.create_or_edit_hosting, name='add_Hosting'),
    path('edit/hosting/<int:hosting_id>/',views.create_or_edit_hosting, name='edit_Hosting'),
    path('Hosting/', HostingListView.as_view(), name='Hosting'),
    path('Hosting-delete/<int:id>/', HostingDeleteView.as_view(), name='deleteHosting'),

    path('add/about',views.add_edit_About, name='add_About'),

    path('add/question',views.add_edit_Question, name='add_Question'),
    path('edit/question/<int:id>/',views.add_edit_Question, name='edit_Question'),
    path('Question/', QuestionListView.as_view(), name='Question'),
    path('Question-delete/<int:id>/', QuestionDeleteView.as_view(), name='deleteQuestion'),

    path('add/client',views.add_edit_Client, name='add_Client'),
    path('edit/client/<int:id>/',views.add_edit_Client, name='edit_Client'),
    path('Client/', ClientListView.as_view(), name='Client'),
    path('Client-delete/<int:id>/', ClientDeleteView.as_view(), name='deleteClient'),

    path('add/herobanner',views.HeroBanners, name='add_HeroBanner'),

    path('add/companydetails',views.CompanyDetailss, name='add_CompanyDetails'),


    path('add/service',views.add_edit_Service, name='add_Service'),
    path('edit/service/<int:id>/',views.add_edit_Service, name='edit_Service'),
    path('Service/', ServiceListView.as_view(), name='Service'),
    path('Service-delete/<int:id>/', ServiceDeleteView.as_view(), name='deleteService'),

    path('userlogout/', views.userlogout, name='userlogout'),

    


]
