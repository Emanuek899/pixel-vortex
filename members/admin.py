from django.contrib import admin
from members.models import CustomUser, OldPassword, Cart, Wishlist, Item_wishlist

class WishlistAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            # Forzar la visualización de todos los usuarios
            kwargs["queryset"] = CustomUser.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(CustomUser)
admin.site.register(OldPassword)
admin.site.register(Cart)
admin.site.register(Wishlist, WishlistAdmin)  # Registrar con la clase personalizada
admin.site.register(Item_wishlist)