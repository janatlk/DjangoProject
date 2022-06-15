from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us',views.page, name='page'),
    path('about-today',views.today, name='today'),
    # path('products',views.product_list_views, name='product'),
    # path('products/<int:id>', views.product_detail_views, name='description')
    path('director',views.director_list,name='directors'),
    path('director/<int:id>',views.director_details,name='details'),
    path('movies',views.movies_list,name='movies'),
    path('movies/<int:id>',views.movies_details,name='movie_detail'),
    path('reviews',views.reviews_list,name='reviews'),
    path('reviews/<int:id>',views.reviews_details,name='reviws_detail')
]
