from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Classification(models.Model):
    classification_id = models.AutoField(primary_key=True)
    classification = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = _("Classification")
        verbose_name_plural = _("Classifications")

    def __str__(self):
        return "{}, {}".format(self.classification_id, self.classification)


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=50, null=False, blank=False) 
    
    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return "{}, {}".format(self.genre_id, self.genre)


class VideogameComment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        "members.CustomUser",
        related_name="users_videogame_comments",
        on_delete=models.CASCADE
    )
    comment = models.CharField(
        max_length=200,
        null=False,
        blank=False)
    community = models.ForeignKey(
        "community.Community",
        related_name="community",
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = _("VideogameComment")
        verbose_name_plural = _("VideogameComments")
    
    def __str__(self):
        return self.comment


class VideogameLike(models.Model):
    like_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        "members.CustomUser",
        related_name="user_videogame_like",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name=_("VideogameLike")
        verbose_name_plural=_("VideogameLikes")
    
    def __str__(self):
        return self.user.username


class Videogame(models.Model):
    videogame_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, unique=True, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    classification = models.ManyToManyField(Classification, related_name="game_classification")
    genre = models.ManyToManyField(Genre, related_name="game_genre")
    platform = models.CharField(choices = [
        ("PC", "Computer"),
        ("X", "Xbox"),
        ("PS", "Play station"),
        ("N", "Nintendo")
    ], blank=False, null=False, max_length=20)
    comments = models.ManyToManyField(
        VideogameComment,
        related_name="videogame_comments", blank=True)
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("Videogame")
        verbose_name_plural = _("Videogames")

    def __str__(self):
        genres = ", ".join([g.genre for g in self.genre.all()]) if self.genre.exists() else "No genre"
        classification = ", ".join([c.classification for c in self.classification.all()]) if self.classification.exists() else "No classification"
        return "{}, {}, {}, {}, {}".format(self.videogame_id, self.name, self.description, genres, classification)


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
    ], max_length=20, default="A")
    game = models.ForeignKey(Videogame, on_delete=models.CASCADE, related_name="Licenses")

    class Meta:
        verbose_name = _("License")
        verbose_name_plural = _("Licenses")

    def __str__(self): 
        product = self.game.name if self.game else "No game selected"
        return "Product: {}, Key: {}".format(product, self.key)

