from django import forms
from django.forms import Form, ModelForm, CharField, TextInput, PasswordInput, ChoiceField, Select, NumberInput,SelectMultiple,DateTimeInput
from FindBikeFriends_app.models import Company,Advertisement,AdvertisementImage


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={'class': 'form-control','placeholder':'Kullanıcı Adı','style':'margin-bottom:20px;'}))
    password = CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Parola', 'name': 'password', 'id': 'password', 'required': 'required', 'autofocus': 'autofocus', 'data-eye': 'data-eye'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")


class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ["name", "description", "start_date", "end_date", "price", "thumbnail"]
        widgets = {
            'name': TextInput(attrs={'class': 'col-sm-7'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'start_date': DateTimeInput(attrs={'class': 'form-control'}),
            'end_date': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
        }



class AdvertisementImageForm(ModelForm):
    class Meta:
        model = AdvertisementImage
        fields = ["image"]


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ( 'first_name', 'last_name','address','link_facebook','link_instagram','link_twitter','link_web','features')

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'link_facebook': TextInput(attrs={'class': 'form-control'}),
            'link_instagram': TextInput(attrs={'class': 'form-control'}),
            'link_twitter': TextInput(attrs={'class': 'form-control'}),
            'link_web': TextInput(attrs={'class': 'form-control'}),
            'features': Select(attrs={'class': 'form-control'}),
        }
