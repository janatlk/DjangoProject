from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from main.models import Movie, Director, ConfirmCode, CustomUser
import secrets
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser as User
from djangoProject.settings import EMAIL_HOST_USER

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
        code = secrets.token_hex(10)
        ConfirmCode.objects.create(user=user, code=code)
        send_mail(subject='Подтверждение E-mail',message=f'''
        Подтверждение E-mail:
        http://127.0.0.1:8000/activate/{code}
        Если вы не совершали никаких действий на сайте САЙТ, просто проигнорируйте это сообщение.
        
        ''',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[email])
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

class EditProfileForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваше имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите вашу фамилию'
    }))
    birthday = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите вашу дату рождения'
    }))

class CustomUserCreationForm(UserCreationForm):
     class Meta:
       model = CustomUser
       fields = UserCreationForm.Meta.fields + ('birthday','gender')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields