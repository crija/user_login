from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('create_user', views.user, name='test_user')
  # path('login', views.login, name='create_login'),
]
