from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from mptt.fields import TreeManyToManyField

from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey

from ..managers import DRAFT, HIDDEN, PUBLISHED
from ...mixins.models.image import ImageMixin
from ..managers.post import PostSet
from ...mixins.models.admin import AdminURLMixin


class CorePost(models.Model, AdminURLMixin):
    """
    class that define a post in the Blog
    """
    STATUS_CHOICES = (
        (DRAFT, _('Borrador')),
        (PUBLISHED, _('Publicado')),
        (HIDDEN, _('Oculto'))
    )

    # region fields

    title = models.CharField(_('título'), max_length=255)

    slug = models.SlugField(_('slug'), max_length=255,
                            help_text=_("Utilizado para construir la Url de la publicación."))

    body = models.TextField(_('contenido'), blank=True)

    creation_date = models.DateTimeField(_('creado'), default=timezone.now)

    publication_date = models.DateTimeField(_('publicado'),
                                            db_index=True, default=timezone.now,
                                            help_text=_("Fecha de publicación."))

    start_publication = models.DateTimeField(_('inicio de publicación'),
                                             db_index=True,
                                             blank=True, null=True,
                                             help_text=_('Fecha de inicio de publicación.'))

    end_publication = models.DateTimeField(_('fín de publicación'),
                                           db_index=True,
                                           blank=True, null=True,
                                           help_text=_('Fecha de fin de publicación.'))

    last_update = models.DateTimeField(_('actualizado'), auto_now=True)

    status = models.IntegerField(_('estatus'), db_index=True,
                                 choices=STATUS_CHOICES, default=DRAFT)

    lead = models.TextField(_('encabezado'), blank=True,
                            help_text=_('Encabezado de la publicación.'))

    excerpt = models.TextField(_('resumen'), blank=True,
                               help_text=_('Usado para el posicionamiento en buscadores.'))

    # tags = TagField(_('etiquetas'))

    featured = models.BooleanField(_('destacado'), default=False)

    objects = PostSet.as_manager()

    comment_enabled = models.BooleanField(_('permitir comentarios'), default=True,
                                          help_text=_('Permite comentarios en caso de estar activado.'))

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def is_actual(self):
        now = timezone.now()
        if self.start_publication and now < self.start_publication:
            return False
        if self.end_publication and now > self.end_publication:
            return False
        return True

    def is_visible(self):
        return self.is_actual() and self.status == PUBLISHED

    @models.permalink
    def get_absolute_url(self):
        return 'blogs:blog:post_detail', (), \
               {'blog_slug': self.blog.slug, 'post_slug': self.slug}

    class Meta:
        """
        Post's meta informations.
        """
        abstract = True
        ordering = ['post_order']
        verbose_name = _('Publicación')
        verbose_name_plural = _('Publicaciones')
        index_together = [['slug', 'publication_date'],
                          ['status', 'publication_date',
                           'start_publication', 'end_publication']]


class BlogPostSortable(SortableMixin):
    blog = SortableForeignKey('Blog',
                              on_delete=models.PROTECT,
                              related_name='posts',
                              verbose_name=_('blog'))

    post_order = models.PositiveIntegerField(default=0,
                                             editable=False,
                                             db_index=True)

    class Meta:
        abstract = True
        ordering = ['post_order']


class AuthorPost(models.Model):
    authors = models.ManyToManyField('Author', related_name='posts',
                                     verbose_name=_('autores'))

    class Meta:
        abstract = True


class SourcePost(models.Model):
    source = models.ForeignKey('Source',
                               on_delete=models.SET_NULL,
                               related_name='posts',
                               null=True, blank=True,
                               verbose_name=_('fuente'))

    class Meta:
        abstract = True


class RelatedPost(models.Model):
    related = models.ManyToManyField('self', blank=True,
                                     related_name='posts',
                                     verbose_name=_('relacionadas'))

    class Meta:
        abstract = True


class ImagePost(ImageMixin):
    """
    Abstract model class to add an image for illustrating the posts.
    """

    class Meta:
        abstract = True


class CategoryPost(models.Model):
    categories = TreeManyToManyField('Category', blank=True,
                                     related_name='posts',
                                     verbose_name=_('categorías'))

    class Meta:
        abstract = True


class TagPost(models.Model):
    tags = models.ManyToManyField('Tag', blank=True,
                                  related_name='posts',
                                  verbose_name=_('etiquetas'))

    class Meta:
        abstract = True


class ReferencePost(models.Model):
    reference = models.ForeignKey('self', on_delete=models.CASCADE,
                                  null=True, blank=True,
                                  related_name='referenced',
                                  verbose_name=_('referencia'))

    class Meta:
        abstract = True


class Post(CorePost, BlogPostSortable, ReferencePost, ImagePost,
           CategoryPost, AuthorPost,
           SourcePost, RelatedPost, TagPost):
    """
    Final model class for a Post representation
    """
