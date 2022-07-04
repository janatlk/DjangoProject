from django import forms
from django.core.exceptions import ValidationError

from main.models import Movie, Director
from django.contrib.auth.forms import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title description director'.split()
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Введите название фильма'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Введите описание фильма'}),
            'director' : forms.Select(attrs={'class':'form-control'})
        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = 'name'.split()
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Введите имя режжисёра'})
        }

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Введите имя пользователя'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Введите Email (Необязательно)'
    }),required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Придумайте пароль'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Повторите пароль'
    }))

    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(username=username)
        if users:
            raise ValidationError('Пользователь с таким именем уже существует!')
        return username

    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise ValidationError('Пароли не совпадают!')
        return password

    def clean_email(self):
        email = self.cleaned_data['email']
        if email != '':
            emails = User.objects.filter(email=email)
            if emails:
                raise ValidationError('Такой email уже зарегестрирован!')
        return email

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username,password=password,email=email,is_active=False)
        return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя либо email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))