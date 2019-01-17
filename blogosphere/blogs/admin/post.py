from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html_join, format_html
from django.contrib import messages

from adminsortable.admin import SortableAdmin
from modeltranslation.admin import TranslationAdmin

from .filters import BlogFilter, CategoryListFilter, AuthorFilter, TagFilter, UserBlogFilter
from .forms import PostForm
from . import get_has_permission
from ..managers import (DRAFT, HIDDEN, PUBLISHED,
                        CAN_CHANGE_STATUS_POST,
                        CAN_EDIT_POST, CAN_DELETE_POST)


class PostAdmin(SortableAdmin, TranslationAdmin):
    list_per_page = 50
    form = PostForm

    fieldsets = ((_('Contenido'), {
        'fields': (
            'title_es', 'title_en', 'title_fr', 'status', 'slug', 'lead_es', 'lead_en', 'lead_fr',
            'body_es', 'body_en', 'body_fr',)}),
                 (_('Ilustración'), {
                     'fields': ('image', 'image_caption_es', 'image_caption_en', 'image_caption_fr',),
                 }),
                 (_('Publicación'), {
                     'fields': ('publication_date', 'blog',
                                ('start_publication', 'end_publication')),
                 }),
                 (_('Comentarios'), {
                     'fields': ('comment_enabled',)
                     ,
                 }),
                 (_('Metadatos'), {
                     'fields': (
                         'featured', 'excerpt_es', 'excerpt_en', 'excerpt_fr', 'authors', 'related', 'source'),
                 }),)

    list_filter = ['publication_date',
                   'status', 'featured',
                   UserBlogFilter,
                   CategoryListFilter,
                   AuthorFilter,
                   TagFilter]

    list_display = ('get_image',
                    'title', 'status',
                    'get_authors',
                    'blog',
                    'featured',
                    'get_categories',
                    'get_tags',
                    'get_is_visible',)

    list_display_links = ('title', 'get_image')

    prepopulated_fields = {'slug': ('title',)}

    # region custom methods

    def get_authors(self, post):
        return format_html_join(
            '\n', '<li><a href="{}">{}</a></li>',
            [(author.get_admin_url(), author.name) for author in post.authors.all()])

    get_authors.short_description = _('autores')

    def get_categories(self, post):
        return format_html_join(
            '\n', '<li><a href="{}">{}</a></li>',
            [(category.get_admin_url(), category.title) for category in post.categories.all()])

    get_categories.short_description = _('categorías')

    def get_is_visible(self, post):
        return post.is_visible()

    get_is_visible.boolean = True
    get_is_visible.short_description = _('visible')

    def get_queryset(self, request):

        qs = super(PostAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(blog__pk__in=request.user.blog_permissions.values_list('blog__pk', flat=True))

        return qs

    def get_tags(self, post):
        """
            Return the tags linked in HTML.
        """

        return format_html_join(
            '\n', '<li><a href="{}">{}</a></li>',
            [(tag.get_admin_url(), tag.name) for tag in post.tags.all()])

    get_tags.short_description = _('etiqueta(s)')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            if obj:
                can_edit = get_has_permission(request, obj.blog, CAN_EDIT_POST)
                can_change_status = get_has_permission(request, obj.blog, CAN_CHANGE_STATUS_POST)

                if can_edit:
                    if can_change_status:
                        return ['featured']
                    else:
                        return ['featured', 'status']
                else:

                    fields = ['title_es', 'title_en', 'title_fr', 'slug', 'status', 'lead_es', 'lead_en', 'lead_fr',
                              'body_es', 'body_en', 'body_fr', 'publication_date', 'blog',
                              'start_publication', 'end_publication', 'image', 'image_caption_es',
                              'image_caption_en', 'image_caption_fr', 'authors',
                              'comment_enabled', 'featured', 'excerpt_es', 'excerpt_en', 'excerpt_fr',
                              'related', 'source', 'categories', 'tags']
                    if can_change_status:
                        fields.remove('status')
                    return fields
        return []

    def save_model(self, request, obj, form, change):
        list(messages.get_messages(request))
        if not request.user.is_superuser:
            if not get_has_permission(request, obj.blog,
                                      CAN_CHANGE_STATUS_POST):
                obj.status = DRAFT
                self.message_user(request, _(
                    'La publicación ha sido marcada como "Borrador", '
                    'Su usuario no tiene permisos para cambiar el estatus.'))
            if not change:
                obj.content_author_id = request.user.id

        super(PostAdmin, self).save_model(request, obj, form, change)

    def get_image(self, blog):
        return format_html('<image src="{}" />',
                           blog.image.thumbnail["50x50"].url)

    get_image.short_description = _('Image')

    def changelist_view(self, request, extra_context=None):
        if request.user.is_superuser:
            self.list_editable = ['featured', 'status']

        return super(PostAdmin, self).changelist_view(request, extra_context)

    def get_actions(self, request):
        if request.user.is_superuser:
            return super(PostAdmin, self).get_actions(request)

        return []

    def get_fieldsets(self, request, obj=None):
        if not request.user.is_superuser:
            return self.fieldsets
        else:
            return ((_('Contenido'), {
                'fields': (
                    'title_es', 'title_en', 'title_fr', 'status', 'slug', 'lead_es', 'lead_en', 'lead_fr',
                    'body_es', 'body_en', 'body_fr',)}),
                    (_('Ilustración'), {
                        'fields': ('image', 'image_caption_es', 'image_caption_en', 'image_caption_fr',),
                    }),
                    (_('Publicación'), {
                        'fields': ('publication_date', 'blog',
                                   ('start_publication', 'end_publication')),
                    }),
                    (_('Comentarios'), {
                        'fields': ('comment_enabled',)
                        ,
                    }),
                    (_('Metadatos'), {
                        'fields': (
                            'featured', 'excerpt_es', 'excerpt_en', 'excerpt_fr', 'authors', 'related', 'source'),
                    }),
                    (None, {'fields': ('categories', 'tags')}),
                    (_('Referenciar'), {'fields': ('reference',)})

                    )

    def has_delete_permission(self, request, obj=None):
        can_delete = super(PostAdmin, self).has_delete_permission(request, obj)

        if obj and not request.user.is_superuser:
            return can_delete and get_has_permission(request, obj.blog, CAN_DELETE_POST)

        return can_delete

    def get_prepopulated_fields(self, request, obj=None):
        if obj and not get_has_permission(request, obj.blog, CAN_EDIT_POST):
            return {}

        return self.prepopulated_fields

    # endregion

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
