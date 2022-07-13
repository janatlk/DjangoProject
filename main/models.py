from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    birthday = models.DateField(default='none')
    gender = models.TextField(default='none')

    def __str__(self):
        return self.username
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
    class Meta:
        verbose_name = 'режиссёр'
        verbose_name_plural = "режиссёры"
    name = models.CharField("Имя режжисёра",max_length=40)

    def __str__(self):
        return self.name

class Movie(models.Model):
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
    title = models.CharField('Название фильма',max_length=100)
    description = models.TextField("Описание",default='None',blank=True)
    director = models.ForeignKey(Director,on_delete=models.SET_NULL,null=True,verbose_name='Режжисёр')
    image = models.ImageField("Изображение",upload_to='movies', null=True)


    def __str__(self):
        return self.title

class Review(models.Model):
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
    text = models.TextField('Отзыв')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,null=True,verbose_name='К фильму')

    def __str__(self):
        return self.text



class ConfirmCode(models.Model):
    code = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.code