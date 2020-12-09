from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Class "UserCreationForm" generates form with "username" and two passwords fields and implements validation.
# Class "SignUpForm" extends "UserCreationForm" with additional fields ("first_name", "..").
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # Typical django pattern to define meta data.
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )

# Class "ModelForm" defaults each field as editable but the field "username" should be read only.
class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']