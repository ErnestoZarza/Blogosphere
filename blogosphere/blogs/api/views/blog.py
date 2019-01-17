from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ParseError

from ..serializers import BlogSerializer

from ..utils import parse_string_to_date
from ...models import Blog


def parse_date_parm(str_date):
    date = parse_string_to_date(str_date)
    if not date:
        raise ParseError(detail='Invalid date format')

    return date


class BlogListAPIView(ListAPIView):

    serializer_class = BlogSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        authors = self.request.query_params.get('authors', None)
        title = self.request.query_params.get('title', None)
        # updated_date = self.request.query_params.get('updated', None)
        # created_date = self.request.query_params.get('created', None)

        blogs = Blog.objects.published()
        if authors is not None:
            blogs = blogs.prefetch_related('author').filter(authors__slug=authors).distinct()
        if q is not None:
            blogs = blogs.filter(title__icontains=q)

        # if updated_date and created_date:
        #     updated_date = parse_date_parm(updated_date)
        #     created_date = parse_date_parm(created_date)
        #     blogs = blogs.exclude(start_date__gt=to_date,
        #                                     end_date__lt=from_date).distinct()
        # elif updated_date:
        #     updated_date = parse_date_parm(updated_date)
        #     blogs = blogs.exclude(created__lt=updated_date).distinct()
        # elif created_date:
        #     created_date = parse_date_parm(created_date)
        #     blogs = blogs.exclude(created__gt=created_date).distinct()

        return blogs
