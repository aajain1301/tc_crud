from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta():
        model = models.User
        fields = ('first_name','last_name','username','desig', 'password1','password2')
