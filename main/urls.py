from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/',views.page, name='page'),
    path('about-today/',views.today, name='today'),
    path('movies/',views.MovieListView.as_view(),name='movies'),
    path('movies/<int:id>/',views.movies_details,name='movie_detail'),
    path('movie_add/',views.movie_add),
    path('director_add/',views.director_add),
    path('register/',views.register),
    path('login/',views.login_view,name='login'),
    path('activate/<str:code>',views.ConfirmView.as_view()),
    path('logout/',views.logout_user.as_view),
    path('profile/',views.profile_view),
    path('editprofile/'
         ,views.Edit_profile.as_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)