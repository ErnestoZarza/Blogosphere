from django.contrib import admin
from django.contrib.admin.utils import flatten
from mptt.admin import DraggableMPTTAdmin

from .forms import CategoryForm


class CategoryAdmin(DraggableMPTTAdmin):
    form = CategoryForm
    fields = (('title', 'slug'),
              'parent', 'description')

    search_fields = ['name']

    prepopulated_fields = {'slug': ('title',)}
