from django.contrib import admin
from .models import Category, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "category", "show")
    list_editable = ("phone", "show")
    list_per_page = 4


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass





