from django.utils import timezone
from django.template.defaultfilters import slugify
from django.db.models import Q, QuerySet
from modeltranslation.manager import MultilingualQuerySet
from . import PUBLISHED


class PostSet(MultilingualQuerySet):

    def published(self):
        now = timezone.now()
        posts = self.filter(
            Q(reference=None) | (
                    (Q(reference__start_publication__lte=now) |
                     Q(reference__start_publication=None) &
                     Q(reference__end_publication__gt=now) |
                     Q(reference__end_publication=None)) &
                    Q(reference__status=PUBLISHED) &
                    Q(reference__blog__status=PUBLISHED)),
            Q(start_publication__lte=now) |
            Q(start_publication=None),
            Q(end_publication__gt=now) |
            Q(end_publication=None),
            status=PUBLISHED, blog__status=PUBLISHED)

        return posts

    def search_published(self, pattern):
        slug_pattern = slugify(pattern)
        return self.published().filter(slug__icontains=slug_pattern,
                                       authors__slug__icontains=slug_pattern,
                                       blog__slug__icontains=slug_pattern).distinct()

    def search_in_blog(self, blog):
        slug_blog = slugify(blog)
        return self.published().filter(blog__slug__icontains=slug_blog).distinct()

    def search_post_in_blog(self, blog, post):
        slug_blog = slugify(blog)
        slug = slugify(post)
        return self.published().filter(slug=slug, blog__slug__icontains=slug_blog).distinct()

    def featured(self):
        return self.filter(featured=True)
