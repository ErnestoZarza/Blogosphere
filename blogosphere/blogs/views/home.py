from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.db.models import Q

from ..models import Post, Blog
from django.shortcuts import render


class Homepage(TemplateView):
    template_name = 'blogs/index.html'

    def get(self, request, *args, **kwargs):
        category_slug = request.GET.get('category', None)
        author_slug = request.GET.get('author', None)
        slug = request.GET.get('slug', None)
        text = self.request.GET.get('text', None)

        # blogs = Blog.objects.published()
        # posts = Post.objects.published()

        # if category_slug:
        #     blogs = blogs.filter(categories__slug__icontains=category_slug).distinct()
        #     posts = posts.filter(categories__slug__icontains=category_slug).distinct()
        #
        # if author_slug:
        #     blogs = blogs.filter(authors__slug__icontains=author_slug).distinct()
        #     posts = posts.filter(authors__slug__icontains=category_slug).distinct()
        #
        # if slug:
        #     blogs = blogs.filter(categories__slug__icontains=category_slug).distinct()
        #     posts = posts.filter(categories__slug__icontains=category_slug).distinct()
        #
        # if text:
        #     q = slugify(text)
        #     blogs = blogs.filter(Q(slug__icontains=q) |
        #                          Q(authors__slug__icontains=q) |
        #                          Q(categories__slug__icontains=q)).distinct()
        #
        #     posts = posts.filter(Q(slug__icontains=q) |
        #                          Q(author__slug__icontains=q) |
        #                          Q(categories__slug__icontains=q)).distinct()

        context = {
            # 'blogs': blogs,
            # 'posts': posts,
        }

        return render(request, self.template_name, context=context)
