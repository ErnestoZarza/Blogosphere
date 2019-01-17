from django.conf.urls import url
from ..views.autocompletes import (BlogAutocomplete, PostAutocomplete, PostTitleAutocomplete, AuthorAutocomplete,
                                   CategoryAutocomplete, SourceAutocomplete, TagAutocomplete,
                                   UserBlogAutocomplete)

urlpatterns = [
    url(r'^blog-autocomplete/$',
        BlogAutocomplete.as_view(),
        name='blog_autocomplete'),

    url(r'^user-blog-autocomplete/$',
        UserBlogAutocomplete.as_view(),
        name='user_blog_autocomplete'),

    url(r'^post-autocomplete/$',
        PostAutocomplete.as_view(),
        name='post_autocomplete'),

    url(r'^post-title-autocomplete/$',
        PostTitleAutocomplete.as_view(),
        name='post_title_autocomplete'),

    url(r'^author-autocomplete/$',
        AuthorAutocomplete.as_view(),
        name='author_autocomplete'),

    url(r'^category-autocomplete/$',
        CategoryAutocomplete.as_view(),
        name='category_autocomplete'),

    url(r'^source-autocomplete/$',
        SourceAutocomplete.as_view(),
        name='source_autocomplete'),

    url(r'^tag-autocomplete/$',
        TagAutocomplete.as_view(),
        name='tag_autocomplete'),

]
