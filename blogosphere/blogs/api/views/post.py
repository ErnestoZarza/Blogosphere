from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ParseError

from ..serializers import PostSerializer

from ..utils import parse_string_to_date
from ...models import Post


def parse_date_parm(str_date):
    date = parse_string_to_date(str_date)
    if not date:
        raise ParseError(detail='Invalid date format')

    return date


class PostListAPIView(ListAPIView):

    serializer_class = PostSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        authors = self.request.query_params.get('authors', None)
        title = self.request.query_params.get('title', None)
        # updated_date = self.request.query_params.get('updated', None)
        # created_date = self.request.query_params.get('created', None)

        posts = Post.objects.published()
        if authors is not None:
            posts = posts.prefetch_related('author').filter(authors__slug=authors).distinct()
        if q is not None:
            posts = posts.filter(title__icontains=q)