from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'spesometro'
urlpatterns = [
    path('', views.simple_upload, name='import'),
]