# Generated by Django 4.0.5 on 2022-06-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_movie_director_review_movie_alter_director_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
