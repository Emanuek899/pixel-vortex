from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Classification(models.Model):
    clasification_id = models.AutoField(primary_key=True)
    clasification = models.CharField(max_length=50, null=False, blank=False)


    class Meta:
        verbose_name = _("Classification")
        verbose_name_plural = _("Classifications")

    def __str__(self):
        return "{}, {}".format(self.clasification_id, self.clasification)



class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=50, null=False, blank=False)
    

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return "{}, {}".format(self.genre_id, self.genre)


class Videogame(models.Model):
    videogame_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, unique=True, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    clasification = models.ManyToManyField(Classification, related_name="game_classification")
    genre = models.ManyToManyField(Genre, related_name="game_genre")
    platform = models.CharField(choices = [
        ("PC", "Computer"),
        ("X", "Xbox"),
        ("PS", "Play station"),
        ("N", "Nintendo")
    ], blank=False, null=False, max_length=20)


    class Meta:
        verbose_name = _("Videogame")
        verbose_name_plural = _("Videogames")

    def __str__(self):
        return "{}, {}, {}".format(self.videogame_id, self.name, self.description)


class License(models.Model):
    license_id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=15, unique=True, null=False, blank=False)
    stock = models.IntegerField(null=False, default=0)
    region = models.CharField(choices=[
        ("WW", "WorldWide"),
        ("EU", "Europe"),
        ("NA", "North America"),
        ("LA", "LATAM"),
        ("AS", "Asia"),
        ("JP", "Japan"),
        ("CN", "China"),
    ], blank=False, null=False, max_length=20)
    price = models.IntegerField(null=False, blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[
        ("A", "Available"),
        ("R", "Redeemed"),
        ("D", "Duplicated"),
    ], max_length=20)
    game = models.ForeignKey(Videogame, on_delete=models.CASCADE, related_name="Licenses")


    class Meta:
        verbose_name = _("License")
        verbose_name_plural = _("Licenses")

    def __str__(self): 
        return self.key







