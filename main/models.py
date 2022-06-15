from django.db import models

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

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()

