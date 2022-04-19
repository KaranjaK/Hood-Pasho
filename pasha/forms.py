from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighborhood, Resident, Business


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        exclude = ('user', 'neighbourhood')


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')