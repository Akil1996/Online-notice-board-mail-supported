# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','department','qualification','destination','address','city','state','country','mobileno','alternativemobileno')
    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','department','qualification','destination','address','city','state','country','mobileno','alternativemobileno')

class EditProfileForm(UserChangeForm):
    password=forms.CharField(label="",widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model =CustomUser 
        fields=('username','first_name','last_name','email','password','department','qualification','destination','address','city','state','country','mobileno','alternativemobileno')