from django.utils.text import slugify
from dal import autocomplete

from ..models import (Blog, Post, Category, Author, Source, Tag, Comment)


class BlogAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        queryset = Blog.objects.all()

        if self.q:
            queryset = queryset.filter(slug__icontains=slugify(self.q)).order_by('name')

        return queryset


class UserBlogAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Blog.objects.all()
        if not self.request.user.is_superuser:
            qs = qs.filter(pk__in=self.request.user.blog_permissions.values_list('blog__pk', flat=True))

        if self.q:
            qs = qs.filter(slug__icontains=slugify(self.q)).order_by('name')
        return qs


class PostAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        queryset = Post.objects.all()

        if self.q:
            queryset = queryset.filter(slug__icontains=slugify(self.q)).order_by('name')

        return queryset


class PostTitleAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        queryset = Post.objects.all()

        if self.q:
            queryset = queryset.filter(slug__icontains=slugify(self.q)).order_by('name')

        return queryset


# class PostTitleAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         queryset = Comment.objects.all()
#
#         if self.q:
#             queryset = queryset.filter(post__slug__icontains=slugify(self.q)).order_by('name')
#
#         return queryset


class AuthorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Author.objects.none()

        queryset = Author.objects.all()

        if self.q:
            queryset = queryset.filter(slug__icontains=slugify(self.q)).order_by('name')

        return queryset


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        queryset = Tag.objects.all()

        if self.q:
            queryset = queryset.filter(slug__icontains=slugify(self.q)).order_by('name')

        return queryset


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        queryset = Category.objects.all()

        if self.q:
            queryset = queryset.filter(slug__icontains=slugify(self.q)).order_by('level', 'title')

        return queryset


class SourceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Source.objects.none()

        queryset = Source.objects.all()

        if self.q:
            queryset = queryset.filter(slug__icontains=slugify(self.q)).order_by('name')

        return queryset
