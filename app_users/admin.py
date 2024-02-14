from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_users.models import User, Payment, PurchasedProduct


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'city_name', 'email', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('date_joined',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(PurchasedProduct)
class PurchasedProductAdmin(admin.ModelAdmin):
    pass
