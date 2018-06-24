from django import forms
from Bookings.models import *

class LoginForm(forms.Form):
    name = forms.CharField(label='Enter Your Name' , max_length=50)
    contact = forms.CharField(label='Mobile No', max_length=10)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())



class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    contact = forms.CharField(label='Contact', max_length=10)
    email = forms.EmailField(label='Email', required=False, max_length=254)
    address = forms.CharField(label='Address', required=False, max_length=200)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    cpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        pas = cleaned_data.get('password')
        cpas = cleaned_data.get('cpassword')
        if pas != cpas:
            msg = "Password did not matched"
            self.add_error('cpassword', msg)


class BookHotelForm(forms.Form):
    location = forms.CharField(label='Location' ,max_length=20)
    amount = forms.FloatField(label='Enter the upper limit of Your Budget')