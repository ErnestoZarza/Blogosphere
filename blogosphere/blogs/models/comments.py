from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..managers import DRAFT, HIDDEN, PUBLISHED
from ..managers.comments import CommentsSet


class CoreComment(models.Model):
    STATUS_CHOICES = (
        (DRAFT, _('Borrador')),
        (PUBLISHED, _('Publicado')),
        (HIDDEN, _('Oculto'))
    )

    name = models.CharField(_('nombre'), max_length=255)

    email = models.CharField(_('correo'), max_length=255)

    content = models.TextField(_('comentario'))

    submit_day = models.DateTimeField(_('fecha'), auto_now_add=True)

    ip = models.GenericIPAddressField(_('ip'))

    status = models.IntegerField(_('estatus'), db_index=True,
                                 choices=STATUS_CHOICES, default=DRAFT)

    object = CommentsSet.as_manager()

    class Meta:
        verbose_name = _('comentario')
        verbose_name_plural = _('comentarios')
        abstract = True

    def __str__(self):
        return '%s : %s' % (self.name, self.get_status_display())


class PostComment(models.Model):
    post = models.ForeignKey('Post', verbose_name=_('publicación'), related_name='comments')

    class Meta:
        abstract = True


class Comment(CoreComment, PostComment):
    """"Final model class for a comment representation"""
