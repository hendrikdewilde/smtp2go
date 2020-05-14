import logging

from django import forms


log = logging.getLogger(__name__)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='password', max_length=100,
                               widget=forms.PasswordInput())
