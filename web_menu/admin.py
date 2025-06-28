from django.contrib import admin
from .models import Items


# Define the ui fields
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status", "price",)
    list_filter = ("status",)
    search_fields = ("meal", "description",)


# Reginster the class
admin.site.register(Items, MenuItemAdmin)
