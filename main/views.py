from django.shortcuts import render, redirect, HttpResponse
from main.models import Review,Movie
from main.forms import MovieForm, DirectorForm

def index(request):
    return render(request, "main/index.html")

def page(request):
    return render(request, "main/page1.html")

def today(request):
    return render(request, "main/today.html")

def movies_list(request):
    movie = Movie.objects.all()
    return render(request,'main/movies.html',context={'movies_list': movie})

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
