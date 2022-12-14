# Generated by Django 3.2.12 on 2022-05-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('poster_path', models.CharField(blank=True, max_length=200, null=True)),
                ('adult', models.BooleanField()),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('original_title', models.CharField(max_length=100)),
                ('original_language', models.CharField(max_length=100)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('vote_count', models.IntegerField(blank=True, null=True)),
                ('vote_average', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
