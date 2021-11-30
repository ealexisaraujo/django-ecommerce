from django.contrib import admin
from . import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """
    Customizing the admin page for the category model
    """
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name','slug')
    list_display_links = ('category_name', 'slug')
    search_fields = ('category_name', 'slug')

admin.site.register(models.Category, CategoryAdmin)