from django import forms
from main.models import Movie, Director

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
