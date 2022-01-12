from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart_id', 'date_added']
    list_display_links = ['id', 'cart_id', 'date_added']
    list_filter = ['date_added']
    search_fields = ['cart_id']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'is_active']

# Register your models here.a
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem,CartItemAdmin)