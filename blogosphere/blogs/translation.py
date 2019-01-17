from modeltranslation.translator import register, TranslationOptions

from .models import Post, Blog, Author

@register(Post)
class PostsTranslationOptions(TranslationOptions):
    fields = ('title', 'lead', 'body',
              'image_caption', 'excerpt', 'slug' )

@register(Blog)
class BlogsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'image_caption', 'slug')


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('description', 'image_caption','slug')
