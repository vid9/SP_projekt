from django import forms


class LoginForm(forms.Form):
  uname = forms.CharField(label='Username:', max_length=64)
  psw = forms.CharField(max_length=64, widget=forms.PasswordInput)