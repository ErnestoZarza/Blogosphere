from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _
from ..views.blog import BlogDetailView, BlogListView
from ..views.post import PostListView, PostDetailView

urlpatterns = [

    url(r'^(?P<post_slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<post_slug>[\w-]+)/list/$', PostDetailView.as_view(), name='post_list'),
    url(r'^list/$', BlogListView.as_view(), name='blog_post_list'),
    url(r'^$', BlogDetailView.as_view(), name='blog_detail'),

]
