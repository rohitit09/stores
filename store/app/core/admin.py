from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display=['phone','name']
    fieldsets=(
        (None,{'fields':('phone','password')}),
        (_('Personal Info'),{'fields':('name',)}),
        (_('permission'),{'fields':('is_active','is_staff','is_superuser')}),
         (_('Imp Dates'),{'fields':('last_login',)}),
    )
    add_fieldsets=(
        (None,{ 
            "classes":('wide',),
            'fields':('phone','password1','password2')
            }
        ),
    )

# Register your models here.
admin.site.register(models.User,UserAdmin)
admin.site.register(models.Category)
admin.site.register(models.Seller)
admin.site.register(models.Customer)
admin.site.register(models.Store)
admin.site.register(models.Orders)
admin.site.register(models.Products)
