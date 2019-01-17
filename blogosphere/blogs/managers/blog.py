from django.utils import timezone
from django.db.models import Q, QuerySet
from django.template.defaultfilters import slugify

from . import PUBLISHED


class BlogSet(QuerySet):
    def published(self):
        return self.filter(status=PUBLISHED)

    def search_published(self, pattern):
        slug_pattern=slugify(pattern)
        return self.published().filter(slug__icontains=slug_pattern,
                                       authors__slug__icontains=slug_pattern).distinct()

    def featured(self):
        return self.filter(featured=True)
