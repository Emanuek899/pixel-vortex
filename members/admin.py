from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from members.models import CustomUser, OldPassword, Cart, Wishlist, Item_wishlist

class WishlistAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            # Forzar la visualización de todos los usuarios
            kwargs["queryset"] = CustomUser.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['username', 'email']
    ordering = ['username']

    # Add customized fields without touch original User model admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('communities', 'preferences', 'licenses')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('communities', 'preferences', 'licenses')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OldPassword)
admin.site.register(Cart)
admin.site.register(Wishlist, WishlistAdmin)  # Registrar con la clase personalizada
admin.site.register(Item_wishlist)