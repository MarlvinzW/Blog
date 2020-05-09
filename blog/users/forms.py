from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import User


class PasswordChange(PasswordChangeForm):
    class Meta:
        widgets = {

        }
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class PictureUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['picture']
