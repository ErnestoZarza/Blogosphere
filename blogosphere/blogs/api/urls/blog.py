from django.conf.urls import url

from ..views import BlogListAPIView

urlpatterns = [
    url(r'^$', BlogListAPIView.as_view(), name='activities'),
]
