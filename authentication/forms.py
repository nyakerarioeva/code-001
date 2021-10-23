from django import forms
from django.contrib.auth.forms import UserCreationForm
from  . models import MyUser

class  UserRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email','profession','username','password1', 'password2')