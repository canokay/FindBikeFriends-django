from django import forms
from django.forms import Form, ModelForm, CharField, TextInput,Textarea, PasswordInput, ChoiceField, Select, NumberInput

from FindBikeFriends_app.models import Contact
class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={'class': 'form-control','placeholder':'Kullanıcı Adı','style':'margin-bottom:20px;'}))
    password = CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Parola', 'name': 'password', 'id': 'password', 'required': 'required', 'autofocus': 'autofocus', 'data-eye': 'data-eye'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'title', 'message', )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder':'Ad Soyad',}),
            'email': TextInput(attrs={'class': 'form-control','placeholder':'Eposta',}),
            'title': TextInput(attrs={'class': 'form-control','placeholder':'Konu',}),
            'message': Textarea(attrs={'class': 'form-control','placeholder':'Mesaj', 'cols':'30','rows':'9'}),
}