from django.contrib import admin
from .forms.author import AuthorForm


class TagAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)

