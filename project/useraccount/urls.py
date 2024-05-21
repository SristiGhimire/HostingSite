from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name="useraccount"
urlpatterns = [
        path('', views.login, name='login'),
        path('userlogout/', views.userlogout, name='userlogout'),
        path('change_password',views.change_password,name='change_password'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


