from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Videogame)
admin.site.register(models.Classification)
admin.site.register(models.Genre)
admin.site.register(models.License)
admin.site.register(models.VideogameComment)
admin.site.register(models.VideogameLike)


