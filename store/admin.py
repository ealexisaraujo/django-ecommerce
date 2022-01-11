from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_filter = ('product','variation_category', 'variation_value', 'is_active')
    search_fields = ('product__product_name', 'variation_category', 'variation_value')
    list_editable = ('is_active',)

# Register your models here.
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation, VariationAdmin)