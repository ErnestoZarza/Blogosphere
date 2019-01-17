from django.urls import reverse
from django.contrib.sitemaps import Sitemap

from .blogs.models import Post, Blog


class BlogDetailSitemap(Sitemap):
    changefreq = "always"
    priority = 0.2

    def items(self):
        return Blog.objects.published()

    def lastmod(self, obj):
        return obj.start_publication

    def location(self, obj):
        return obj.get_absolute_url()


class BlogListSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return ['blogs:blog:list']

    def location(self, obj):
        return reverse(obj)


class PostDetailSitemap(Sitemap):
    changefreq = "always"
    priority = 0.2

    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.start_publication

    def location(self, obj):
        return obj.get_absolute_url()


class PostListSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return ['blogs:post:list']

    def location(self, obj):
        return reverse(obj)

class HomepageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['homepage:homepage']

    def location(self, obj):
        return reverse(obj)
