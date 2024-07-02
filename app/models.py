from django.db import models
from django import forms

class Register(models.Model):
    email = models.EmailField(max_length=254)
    hashed_password = forms.CharField(widget=forms.PasswordInput)