from django.contrib import admin
from .models import *
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display=['id', 'genre',]
admin.site.register(Genre, GenreAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display=['id', 'director',]
admin.site.register(Director, DirectorAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display=['id', 'actor',]
admin.site.register(Actor, ActorAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'openingDate', 'audience', 'director',]
admin.site.register(Movie, MovieAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=['id', 'movie', 'content', 'score']
admin.site.register(Comment, CommentAdmin)

