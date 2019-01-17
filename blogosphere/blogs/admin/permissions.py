from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from ..models import UserBlogPermission, BlogPermission
from .forms.user import UserBlogForm


class UserBlogPermissionInline(admin.TabularInline):
    fields = ('user', 'blog', 'permissions')
    list_display = ['user', 'blog', 'permissions']
    model = UserBlogPermission
    filter_horizontal = ['permissions']
    min_num = 0
    extra = 1
    form = UserBlogForm


class CustomUserAdmin(UserAdmin):
    inlines = [UserBlogPermissionInline]


class BlogPermissionsAdmin(admin.ModelAdmin):
    fields = ('permission',)
