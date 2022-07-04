from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

# class Product(models.Model):
#     title = models.CharField("", max_length=50)
#     description = models.TextField(blank=True,default='Отсутсвует')
#     price = models.FloatField()
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title

class Director(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='None',blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='movies', null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return list(self.text)[:10]

# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     auth_token = models.CharField(max_length=100)
#     is_verified = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.username