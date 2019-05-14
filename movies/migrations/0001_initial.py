# Generated by Django 2.1.8 on 2019-05-13 21:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('openingDate', models.DateField()),
                ('audience', models.IntegerField()),
                ('nationality', models.TextField()),
                ('distributor', models.TextField()),
                ('runningTime', models.TextField()),
                ('movieRating', models.TextField()),
                ('description', models.TextField()),
                ('poster_url', models.TextField()),
                ('actors', models.ManyToManyField(blank=True, related_name='movies', to='movies.Actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Director')),
                ('genres', models.ManyToManyField(blank=True, related_name='movies', to='movies.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]