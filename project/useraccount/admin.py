from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import mark_safe
from useraccount.models import User


class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'firstname', 'lastname', 'avatar', 'phone_No', 'is_user', 'is_admin', 'is_subAdmin')
    list_editable = ('is_admin',)
    list_filter = ('is_admin', 'is_user')
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname', 'lastname', 'phone_No', 'avatar')}),
        ('Permissions', {'fields': ('is_admin', 'is_user', 'is_subAdmin')}),  # Exclude groups and user_permissions
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'lastname', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()
    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="100" height="100">')
    image_tag.short_description = 'Avatar'
admin.site.register(User, UserModelAdmin)