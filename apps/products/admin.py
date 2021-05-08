from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'categories']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

admin.site.register(Product, ProductAdmin)