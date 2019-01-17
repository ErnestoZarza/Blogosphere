from django.template import Library

from ..models import Blog, Post

register = Library()


@register.inclusion_tag('blogs/tags/main-post-area.html')
def main_post_area(blog=''):
    if not blog:
        post = Post.objects.published().featured()
    else:
        post = Post.objects.search_published(blog).featured()

    post_main = post.first()
    post_secondaries = post[1:4]

    return {'post_main': post_main, 'post_secondaries': post_secondaries}


@register.inclusion_tag('blogs/tags/featured-blog-area.html')
def featured_blog_area(blog='', count=3):
    if not blog:
        posts = Post.objects.published().featured()
        blog = 'Varios'
    else:
        posts = Post.objects.search_in_blog(blog)

    return {'posts': posts[0:count], 'blog': blog}


@register.inclusion_tag('blogs/tags/latest-posts.html')
def latest_post(blog='', count=6):
    if not blog:
        posts = Post.objects.published().order_by('publication_date')
    else:
        posts = Post.objects.search_in_blog(blog).order_by('publication_date')

    return {'posts': posts[0:count], }


@register.simple_tag
def get_post_or_reference(post):
    if not post.reference:
        return post
    else:
        return post.reference

@register.inclusion_tag('blogs/tags/blog-post-list.html')
def blog_post_list(posts):
    return {'posts':posts}


# @register.inclusion_tag('billboard/sidebar/module-text.html')
# def get_latest(count=5):
#     activities = Activity.objects.published().order_by('activity_order')
#
#     return {'activities': activities[:count]}
