from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us',views.page, name='page'),
    path('about-today',views.today, name='today'),
    path('movies',views.movies_list,name='movies'),
    path('movies/<int:id>',views.movies_details,name='movie_detail'),
    path('movie_add',views.movie_add),
    path('director_add',views.director_add),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)