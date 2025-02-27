from django.contrib import admin
from members.models import CustomUser, OldPassword, Cart, Wishlist, Item_wishlist
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(OldPassword)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Item_wishlist)