from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['subject', 'message']
        widgets = {

            'subject': forms.TextInput(attrs={"class": "form-control input-lg", 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Message', 'rows': '4', 'cols': '25', 'style': 'height: 170px;'}),
        }


class RegisterForm(UserCreationForm):
    # Login form for django standart user model

    class Meta:

        model = User
        fields = ['username','email', 'password1', 'password2']
        widgets = {
            'username':forms.TextInput(attrs={"class":"form-control"}),
            'email':forms.EmailInput(attrs={"class":"form-control"}),
            'password1':forms.PasswordInput(attrs={"class":"form-control"}),
            'password2':forms.PasswordInput(attrs={"class":"form-control"}),
        }


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def username_clean(self):
    #     username = self.cleaned_data['username'].lower()
    #     new = User.objects.filter(username=username)
    #     if new.count():
    #         raise ValidationError("User Already Exist")
    #     return username

    # def email_clean(self):
    #     email = self.cleaned_data['email'].lower()
    #     new = User.objects.filter(email=email)
    #     if new.count():
    #         raise ValidationError(" Email Already Exist")
    #     return email

    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']

    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Password don't match")
    #     return password2

    # def save(self, commit=True):
    #     user = User.objects.create(
    #         username=self['username'],
    #         email=self['email'],
    #         password=self['password1']
    #     )
    #     print('no')
    #     # print(user)
    #     user.save()
    #     # self.save()
    #     return user
