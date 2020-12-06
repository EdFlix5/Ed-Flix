from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.exceptions import ValidationError


class EdFlixUserAuthenticationForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
            )
        return user



class EdFlixUserCreationForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user