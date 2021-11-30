from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

class AccountAdmin(UserAdmin):
    """
    Customizing the admin page for the user model
    """
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login','date_joined','is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    ordering =('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(models.Account, AccountAdmin)