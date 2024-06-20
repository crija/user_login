from django.contrib import admin
from django.urls import path
from app import view

urlpatterns = [
    path('login', view.login, name='create_login'),
]
