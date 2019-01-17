from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import SortableMixin

from ..managers import DRAFT, HIDDEN, PUBLISHED
from ..managers.blog import BlogSet
from ...mixins.models.image import ImageMixin, BannerMixin
from ...mixins.models.admin import AdminURLMixin


class CoreBlog(SortableMixin, AdminURLMixin):
    """
        class that define a Blog
    """
    STATUS_CHOICES = (
        (DRAFT, _('Borrador')),
        (PUBLISHED, _('Publicado')),
        (HIDDEN, _('Oculto'))
    )

    # region fields

    title = models.CharField(_('título'), max_length=255)

    slug = models.SlugField(_('slug'), max_length=255,
                            unique=True, db_index=True,
                            help_text=_("Utilizado para construir la Url del blog."))

    status = models.IntegerField(_('estatus'), db_index=True,
                                 choices=STATUS_CHOICES, default=DRAFT)

    description = models.TextField(_('descripción'), blank=True)

    created = models.DateTimeField(_('creado'), auto_now_add=True)

    updated = models.DateTimeField(_('actualizado'), auto_now=True)

    featured = models.BooleanField(_('destacado'), default=False)

    blog_order = models.PositiveIntegerField(default=0,
                                             editable=False,
                                             db_index=True)

    objects = BlogSet.as_manager()

    # endregion

    # region custom methods

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url_datail(self):

        return 'blogs:blog:blog_detail', (), {'blog_slug': self.slug}
        # return 'blogosphere:blogs:blog_detail', (), {'blog_slug': self.slug}

    def get_absolute_url_list(self):

        return 'blogs:blog:blog_list', (), {'blog_slug': self.slug}
        # return 'blogosphere:blogs:blog_list', (), {'blog_slug': self.slug}

    # endregion

    class Meta:
        abstract = True
        ordering = ['blog_order']
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


class BlogAuthor(models.Model):

    authors = models.ManyToManyField('Author',
                                     related_name='blogs',
                                     verbose_name=_('autores'))

    class Meta:
        abstract = True


class ImageBlog(ImageMixin):
    """
    Abstract model class to add an image for illustrating the blogs.
    """

    class Meta:
        abstract = True


class BannerImageBlog(BannerMixin):
    """
     model class to add a banner image for illustrating the blogs.
    """

    class Meta:
        abstract = True


class Blog(CoreBlog, BannerImageBlog,
           ImageBlog, BlogAuthor):
    """
    Final model class for a Blog representation
    """
