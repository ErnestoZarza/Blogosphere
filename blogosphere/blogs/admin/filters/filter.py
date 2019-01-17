from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from .autocomplete import AutocompleteFilter
from ...models import (Blog, Source, Category, Author, Post, Tag, Comment)


class BlogFilter(AutocompleteFilter):
    title = _('blog')
    param_name = 'blog'
    queryset_filter = Blog.objects.all()
    autocomplete_url = 'blogs:autocompletes:blog_autocomplete'
    widget_attrs = {'data-placeholder': '%s...' % _('Blog')}

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(blog__pk=self.value)

        return queryset


class UserBlogFilter(AutocompleteFilter):
    title = _('blog')
    param_name = 'blog'
    queryset_filter = Blog.objects.all()
    autocomplete_url = 'blogs:autocompletes:user_blog_autocomplete'
    widget_attrs = {'data-placeholder': '%s...' % _('Blog')}

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(blog__pk=self.value())

        return queryset


class PostFilter(AutocompleteFilter):
    title = _('publicación')
    param_name = 'post'
    queryset_filter = Post.objects.all()
    autocomplete_url = 'blogs:autocompletes:post_autocomplete'
    widget_attrs = {'data-placeholder': '%s...' % _('Publicación')}

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(post__pk=self.value())

        return queryset


class CommentListFilter(AutocompleteFilter):
    title = _('publicación')
    param_name = 'post'
    queryset_filter = Post.objects.all()
    autocomplete_url = 'blogs:autocompletes:post_title_autocomplete'
    widget_attrs = {'data-placeholder': '%s...' % _('Publicación')}

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(post__pk=self.value())#.order_by('submit_day')

        return queryset


class AuthorFilter(AutocompleteFilter):
    title = _('autor')
    param_name = 'authors'
    queryset_filter = Author.objects.all()
    autocomplete_url = 'blogs:autocompletes:author_autocomplete'
    widget_attrs = {'data-placeholder': '%s...' % _('Autor')}

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(authors__pk=self.value())

        return queryset


class TagFilter(AutocompleteFilter):
    title = _('etiqueta')
    param_name = 'tags'
    queryset_filter = Tag.objects.all()
    autocomplete_url = 'blogs:autocompletes:tag_autocomplete'
    widget_attrs = {'data-placeholder': '%s...' % _('Etiqueta')}

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(tags__pk=self.value())

        return queryset


class CategoryListFilter(AutocompleteFilter):
    title = _('categoría')
    param_name = 'categories'
    queryset_filter = Category.objects.all()
    autocomplete_url = 'blogs:autocompletes:category_autocomplete'
    widget_attrs = {
        'data-placeholder': '%s...' % _('Categoría')
    }

    def queryset(self, request, queryset):
        if self.value():
            categories = Category.objects.filter(pk=self.value()).get_descendants(include_self=True)
            return queryset.prefetch_related('categories').filter(categories__in=categories).distinct()
        else:
            return queryset


class SingleCategoryListFilter(AutocompleteFilter):
    title = _('categoría')
    param_name = 'category'
    queryset_filter = Category.objects.all()
    autocomplete_url = 'blogs:autocompletes:category_autocomplete'
    widget_attrs = {
        'data-placeholder': '%s...' % _('Categoría')
    }

    def queryset(self, request, queryset):
        if self.value():
            categories = Category.objects.filter(pk=self.value()).get_descendants(include_self=True)
            return queryset.select_related('category').filter(category__in=categories).distinct()
        else:
            return queryset


class SourceFilter(AutocompleteFilter):
    title = _('fuente')
    param_name = 'source'
    queryset_filter = Source.objects.all()
    autocomplete_url = 'blogs:autocompletes:source_autocomplete'
    widget_attrs = {'data-placeholder': '%s...' % _('Fuente')}

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(source__pk=self.value())

        return queryset
