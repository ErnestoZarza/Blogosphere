from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html, format_html_join

from django.core.urlresolvers import reverse

from adminsortable.admin import SortableAdmin
from modeltranslation.admin import TranslationAdmin

from . import get_has_permission
from .filters import AuthorFilter, PostFilter
from .forms import BlogForm
from ..managers import CAN_DELETE_BLOG, CAN_EDIT_BLOG, CAN_CHANGE_STATUS_BLOG


class BlogAdmin(SortableAdmin, TranslationAdmin):
    form = BlogForm
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'status', 'description',)}),
        (_('Imágenes'), {'fields': ('image', 'banner_image')}),
        (_('Publicación'), {
            'fields': ('featured', 'authors'),  # , 'tags'
        }),
    )

    date_hierarchy = 'updated'

    list_display = ('get_image', 'title', 'get_authors',
                    'featured',
                    'status', 'link_to_add_entry',
                    'link_to_post')  # 'get_tags',

    prepopulated_fields = {'slug': ('title',)}

    list_filter = ['created', 'status', 'featured', PostFilter, AuthorFilter]

    actions = ['make_published', 'make_hidden', 'make_draft',
               'mark_featured', 'unmark_featured']

    actions_on_top = False

    list_display_links = ('title', 'get_image')

    def get_authors(self, blog):
        """
        Return the owners in HTML.
        """
        return format_html_join(
            '\n', '<li><a href="{}">{}</a></li>',
            [(author.get_admin_url(), author.name) for author in blog.authors.all()])

    def get_queryset(self, request):
        """
        Make filtering by user's permissions.
        """
        qs = super(BlogAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(pk__in=request.user.blog_permissions.values_list('blog__pk', flat=True))

        return qs

    def link_to_add_entry(self, blog):
        redirect_url = reverse('admin:blogs_post_add')
        extra = '?blog=%s' % blog.id
        return format_html('<a href="{}">%s</a>' % _('Añadir publicación al blog'),
                           (redirect_url + extra))

    link_to_add_entry.short_description = _('Añadir publicación')

    def link_to_post(self, blog):
        redirect_url = reverse('admin:blogs_post_changelist')
        extra = '?blog=%s' % blog.id
        return format_html('<a href="{}">%s ({})</a>' % _('Publicaciones por blog'),
                           (redirect_url + extra), blog.posts.count())

    link_to_post.short_description = _('Publicaciones')

    def get_prepopulated_fields(self, request, obj=None):
        if obj and not get_has_permission(request, obj, CAN_EDIT_BLOG):
            return {}

        return self.prepopulated_fields

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            if obj:
                can_edit = get_has_permission(request, obj, CAN_EDIT_BLOG)
                can_change_status = get_has_permission(request, obj, CAN_CHANGE_STATUS_BLOG)

                if can_edit:
                    if can_change_status:
                        return ['featured']
                    else:
                        return ['featured', 'status']
                else:
                    fields = ['title', 'slug', 'status', 'description', 'image', 'image_caption', 'banner_image',
                              'featured', 'authors']
                    if can_change_status:
                        fields.remove('status')

                    return fields

        return []

    def get_image(self, blog):
        return format_html('<image src="{}" />',
                           blog.image.thumbnail["50x50"].url)

    get_image.short_description = _('Imagen')

    def changelist_view(self, request, extra_context=None):
        if request.user.is_superuser:
            self.list_editable = ['featured', 'status']

        return super(BlogAdmin, self).changelist_view(request, extra_context)

    def get_actions(self, request):
        if request.user.is_superuser:
            return super(BlogAdmin, self).get_actions(request)

        return []

    def has_delete_permission(self, request, obj=None):
        can_delete = super(BlogAdmin, self).has_delete_permission(request, obj)

        if obj and not request.user.is_superuser:
            return can_delete and get_has_permission(request, obj, CAN_DELETE_BLOG)

        return can_delete

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
