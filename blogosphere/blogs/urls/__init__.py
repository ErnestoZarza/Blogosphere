from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy
from django.conf.urls.i18n import i18n_patterns

from ..views.post import PostListView
from ..views.home import Homepage

#
# def i18n_url(url):
#     """
#     Translate an URL part.
#     """
#     return ugettext_lazy(url)


# _ = i18n_url
# urlpatterns = [url(r'^autocompletes/', include('blogosphere.blogs.urls.autocompletes', namespace='autocompletes')), ]
# urlpatterns += i18n_patterns(
#     url(r'^(?P<blog_slug>[\w-]+)/', include('blogosphere.blogs.urls.blog', namespace='blog')),
#     url(r'^list/$', PostListView.as_view(), name='post_list'),
#     url(r'^$', Homepage.as_view(), name='homepage'),
# )

urlpatterns = [url(r'^autocompletes/', include('blogosphere.blogs.urls.autocompletes', namespace='autocompletes')),
               url(r'^(?P<blog_slug>[\w-]+)/', include('blogosphere.blogs.urls.blog', namespace='blog')),
               url(r'^list/$', PostListView.as_view(), name='post_list'),
               url(r'^$', Homepage.as_view(), name='homepage'),]