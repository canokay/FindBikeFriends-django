from django import forms
from django.forms import Form, CharField, TextInput, PasswordInput, ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(Form):
    username = CharField(label="Username", widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label="Password", widget=PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'id': 'password', 'required': 'required'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
