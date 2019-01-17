from django.contrib import admin


class SourceAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'url')
    list_display = ('name', 'slug', 'url')
    search_fields = ('name', 'url')
    prepopulated_fields = {'slug': ('name',)}
