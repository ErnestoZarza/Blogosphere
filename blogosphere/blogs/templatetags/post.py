from django.template import Library

from ..models import Blog, Post, Comment

register = Library()


@register.inclusion_tag('blogs/tags/post-detail-view.html')
def post_detail_view(post):
    return {'post': post}


@register.simple_tag
def get_comments_post(post):
    comments = _('sin comentarios')
    count = 0

    if post:
        comments = Comment.objects.filter(post__pk=post.pk)

    return comments, count
