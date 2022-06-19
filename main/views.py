from django.shortcuts import render
from django.http import HttpResponse
from main.models import Director,Review,Movie


def index(request):
    return render(request, "main/index.html")

def page(request):
    return render(request, "main/page1.html")

def today(request):
    return render(request, "main/today.html")

# def product_list_views(request):
#     product = Product.objects.all() #QuerySet list that came from base
#     context = {
#         'product_list' : product
#     }
#     return render(request,'main/products.html', context=context)
#
#
# def product_detail_views(request,id):
#     product = Product.objects.get(id=id)
#     return render(request,'main/detail.html', context={'product_detail' : product})

# def director_list(request):
#     director = Director.objects.all()
#     return render(request,'main/directors.html',context={'director_list':director})
#
# def director_details(request,id):
#     director = Director.objects.get(id=id)
#     return render(request,'main/directordetail.html',context={'director_detail':director})

def movies_list(request):
    movie = Movie.objects.all()
    return render(request,'main/movies.html',context={'movies_list': movie})

def movies_details(request,id):
    context = {
    'movie_detail' : Movie.objects.get(id=id),
    'review' : Review.objects.filter(movie_id=id)
    }
    # reviews = Review.objects.filter()
    return render(request,'main/moviedetail.html',context=context)

# def movie_filter_view(request,movieid):
#     context = {
#         'reviews':Review.objects.filter(movie_id=movieid)
#     }
#     return render(request,'main/moviedetail.html',context=context)

# def reviews_list(request):
#     # reviews = Review.objects.all()
#     reviews = Review.objects.order_by('-id')
#     return render(request,'main/reviews.html',context={'reviews_list':reviews})
#
# def reviews_details(request,id):
#     reviews = Review.objects.get(id=id)
#     return render(request,'main/reviewdetail.html',context={'reviews_details': reviews})