from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)