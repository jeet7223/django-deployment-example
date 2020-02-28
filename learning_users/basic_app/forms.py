from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from django.core import validators

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    conf_password =forms.CharField(widget=forms.PasswordInput())


    def clean(self):
         all_clean_data = super().clean()
         password = all_clean_data['password']
         conf_password = all_clean_data['conf_password']

         if password != conf_password:
             raise forms.ValidationError('password not same')

    class Meta():
        model = User
        fields = ('username','email','password','conf_password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
