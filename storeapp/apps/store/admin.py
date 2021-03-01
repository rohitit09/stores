from django.contrib import admin


from .models import Store, Category,Products,Orders,Customer


admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Customer)

# Register your models here.
