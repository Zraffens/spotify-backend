from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    ordering = ('-created',)
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    list_display = ('email', 'is_active', 'is_staff',)
    fieldsets = (
        ('Userinfo', {'fields': ('username', 'email', 'is_active')}),
        ('Other Info', {'fields': ('favorites',)})
    )

admin.site.register(MyUser, UserAdminConfig)
