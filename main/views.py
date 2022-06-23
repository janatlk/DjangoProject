from django.shortcuts import render
from main.models import Review,Movie

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