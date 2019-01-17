# methods
def get_has_permission(request, blog, permission):
    return request.user.blog_permissions.filter(blog=blog,
                                                permissions__permission=permission).exists()


from django.contrib import admin
from django.contrib.auth.models import User

from .post import PostAdmin
from .blog import BlogAdmin
from .author import AuthorAdmin
from .category import CategoryAdmin
from .source import SourceAdmin
from .permissions import CustomUserAdmin, BlogPermissionsAdmin
from .comment import CommentAdmin
from .tag import TagAdmin

from ..models import (Post, Blog, Author, Category,
                      Source, BlogPermission,  # UserBlogPermission,
                      Comment, Tag)

# custom models
admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)

# permissions
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(BlogPermission, BlogPermissionsAdmin)
