from django.contrib import admin
from .models import Category, Contact


class ContatoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category)
admin.site.register(Contact)
