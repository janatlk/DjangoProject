from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us',views.page, name='page'),
    path('about-today',views.today, name='today')
]
