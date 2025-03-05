from django.db import models
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    preferences = models.ManyToManyField('polls.Genre', related_name="preferences",  blank=True)  # Usamos `apps.get_model` para evitar el ciclo
    licenses = models.ManyToManyField('polls.License', related_name="user_licenses", blank=True)  # Usamos `apps.get_model` también
    groups = models.ManyToManyField('auth.Group', related_name="customuser_groups")
    user_permissions = models.ManyToManyField('auth.Permission', related_name="customuser_permissions")


    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

    def __str__(self):
        return self.username


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
    

class Cart(models.Model):
    cart_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, related_name="user_cart", on_delete=models.CASCADE)
    product = models.ForeignKey('polls.License', related_name="license_product", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return self.name    
    
# <Cart model> this only defines the cart
class Wishlist(models.Model):
    wishlist_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, related_name="user_wishlist", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Wishlist")
        verbose_name_plural = _("Wishlists")

    def __str__(self):
        user = self.user.username if self.user else "No user selected"
        return "User: {}, Wishlist: {}".format(user, self.wishlist_id)


# <Item_wishlist> This defines the item in the wishlist
class Item_wishlist(models.Model):
    item_wishlist = models.BigAutoField(primary_key=True)
    wishlist = models.ForeignKey(Wishlist, related_name="wish_items", on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('polls.Videogame', related_name="wish_products", on_delete=models.CASCADE)  # Usar 'apps.get_model'

    class Meta:
        verbose_name = _("Item_wishlist")
        verbose_name_plural = _("Item_wishlists")

    def __str__(self):
        wishlist = self.wishlist.wishlist_id if self.wishlist else "No wishlist"
        product = self.product.name if self.product else "No game selected"
        return "{}, {}".format(wishlist, product)