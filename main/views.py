from django.shortcuts import render, redirect, HttpResponse
from main.models import Review,Movie,ConfirmCode
from main.forms import MovieForm, DirectorForm, RegisterForm, LoginForm, EditProfileForm
from django.contrib.auth import login,logout,authenticate
from .models import CustomUser as User
from django.contrib.auth.tokens import default_token_generator
from django.db import models
from django.views import View
from django.views.generic import ListView,FormView
from django.contrib.auth.views import LogoutView


class ConfirmView(View):
    def get(self,request,*args,**kwargs):
        confirm_code = None
        try:
            confirm_code = ConfirmCode.objects.get(code=kwargs['code'])
            user = confirm_code.user
            user.is_active = True
            user.save()
            return HttpResponse("<h1>Подтверждение прошло успешно</h1>")
        except:
            return HttpResponse('<p>Ошибка</p>')

def index(request):
    return render(request, "main/index.html")

def page(request):
    return render(request, "main/page1.html")


def today(request):
    return render(request, "main/today.html")

class MovieListView(ListView):
    queryset = Movie.objects.all()
    template_name = 'main/movies.html'
    context_object_name = 'movies_list'

def movies_details(request,id):
    context = {
    'movie_detail' : Movie.objects.get(id=id),
    'review' : Review.objects.filter(movie_id=id)
    }
    return render(request,'main/moviedetail.html',context=context)

def movie_add(request):
    if request.method == 'GET':
        form = MovieForm()
        return render(request,'main/movieadd.html',context={'form':form})
    elif request.method == 'POST':
        form = MovieForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/movies")
        return render(request,"main/movieadd.html", context={'form':form})


def director_add(request):
    if request.method == 'GET':
        form = DirectorForm()
        return render(request, 'main/directoradd.html', context={'form': form})
    elif request.method == 'POST':
        form = DirectorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/director_add")
        return render(request, "main/directoradd.html", context={'form': form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            User.is_active = models.BooleanField(default=False)
            form.save()
            return redirect('/register/')
    return render(request,'main/register.html',context={'form':form})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request, user=user)
        return redirect('/login/')
    return render(request,'main/login.html',context={'form':form})

def profile_view(request):
    print(request.user.first_name+'l')
    user = User.objects.get(username=request.user.username)
    user.first_name = 'Alex'
    user.save()
    return render(request,'main/profile.html')


# def movies_list(request):
#     movie = Movie.objects.all()
#     return render(request,'main/movies.html',context={'movies_list': movie})

class Edit_profile(FormView):
    form_class = EditProfileForm
    template_name = 'main/editform.html'
    success_url = '/profile/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)





class logout_user(View):
    def logout_user(self,request):
        logout(request)
        return redirect('/')