# Generated by Django 4.0.5 on 2022-06-15 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_director_movies_review_delete_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
