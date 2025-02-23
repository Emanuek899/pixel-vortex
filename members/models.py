from django.db import models
from django.contrib.auth.models import AbstractUser
from polls.models import Genre, License
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.apps import apps
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class CustomUser(AbstractUser):
    communities = models.ManyToManyField("community.Community", related_name = "members")
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False)
    preferences = models.ManyToManyField(Genre, related_name="preferences")
    licenses = models.ManyToManyField(License, related_name="user_licenses")
    
    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions")


    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

    def __str__(self):
        return self.name


class OldPassword(models.Model):
    old_password_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="old_passwords")
    password_hash = models.CharField(max_length=128)
    change_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = _("OldPassword")
        verbose_name_plural = _("OldPasswords")

    def __str__(self):
        return self.name
    

