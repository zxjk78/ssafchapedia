# Generated by Django 3.2.12 on 2022-05-23 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_movie_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]
