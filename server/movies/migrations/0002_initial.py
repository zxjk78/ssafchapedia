# Generated by Django 3.2.12 on 2022-05-23 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_ids',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
    ]
