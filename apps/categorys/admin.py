from django.contrib import admin

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)