from django.contrib import admin
from .models import Item

# Creation of items to be displayed and how in Admin Interface
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")

# Coupling the items above with the DB model
admin.site.register(Item, MenuItemAdmin)