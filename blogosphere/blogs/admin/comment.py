from django.contrib import admin
from django.contrib.admin.utils import flatten
from django.utils.translation import ugettext_lazy as _

from . import get_has_permission
from .forms import CommentForm
from ..managers import (CAN_DELETE_COMMENT, CAN_CHANGE_STATUS_COMMENT,
                        DRAFT, HIDDEN, PUBLISHED)

from .filters import CommentListFilter


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'post','status')
    fields = (('name', 'status'), 'email', 'content', 'post', 'submit_day', 'ip',)

    list_filter = ['submit_day', 'status', CommentListFilter]

    def get_readonly_fields(self, request, obj=None):
        fields = flatten(self.fields)
        if (obj and get_has_permission(request, obj.post.blog, CAN_CHANGE_STATUS_COMMENT)) or request.user.is_superuser:
            fields.remove('status')
            return fields

        return fields

    def has_delete_permission(self, request, obj=None):
        can_delete = super(CommentAdmin, self).has_delete_permission(request, obj)

        if obj and not request.user.is_superuser:
            return can_delete and get_has_permission(request, obj.post.blog, CAN_DELETE_COMMENT)

        return can_delete

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        if request.user.is_superuser:
            return super(CommentAdmin, self).get_actions(request)

        return []

    def changelist_view(self, request, extra_context=None):
        if request.user.is_superuser:
            self.list_editable = ['status']

        return super(CommentAdmin, self).changelist_view(request, extra_context)

    class Media:
        pass