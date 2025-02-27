from django.contrib import admin
from polls.models import Videogame, Classification, Genre, License
# Register your models here.

admin.site.register(Videogame)
admin.site.register(Classification)
admin.site.register(Genre)
admin.site.register(License)

