from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.html import format_html, format_html_join
from django.utils.translation import ugettext_lazy as _

from modeltranslation.admin import TranslationAdmin


from .forms.author import AuthorForm


class AuthorAdmin(TranslationAdmin):
    form = AuthorForm

    fields = (('name','featured',),
              'slug',
              'nickname',
              'image',
              'description',
              'email',
              )

    list_display = ('get_image', 'name', 'nickname', 'slug', 'email',)

    prepopulated_fields = {'slug': ('name',)}

    search_fields = ['name', 'nickname']

    list_display_links = ('name', 'get_image')

    def get_image(self, blog):
        return format_html('<image src="{}" />',
                           blog.image.thumbnail["50x50"].url)

    get_image.short_description = _('Imagen')

    actions_on_top = True
    # actions = True
