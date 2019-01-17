from django.db import models
from django.conf import settings
from django.utils.text import ugettext_lazy as _

from ..managers import (CAN_CHANGE_STATUS_BLOG, CAN_CHANGE_STATUS_COMMENT,
                        CAN_CHANGE_STATUS_POST, CAN_DELETE_BLOG, CAN_DELETE_COMMENT,
                        CAN_DELETE_POST, CAN_EDIT_BLOG, CAN_EDIT_POST, CAN_REFERENCE_POST)


class BlogPermission(models.Model):
    PERMISSION_CHOICES = (
        (CAN_EDIT_BLOG, _('Puede editar blog')),
        (CAN_EDIT_POST, _('Puede editar publicación')),
        (CAN_CHANGE_STATUS_BLOG, _('Puede editar el estatus del blog')),
        (CAN_CHANGE_STATUS_POST, _('Puede editar el estatus de la publicación')),
        (CAN_CHANGE_STATUS_COMMENT, _('Puede editar el estatus del comentario')),
        (CAN_DELETE_BLOG, _('Puede eliminar blog')),
        (CAN_DELETE_POST, _('Puede eliminar publicación')),
        (CAN_DELETE_COMMENT, _('Puede eliminar comentario')),
        (CAN_REFERENCE_POST, _('Puede crear referencias a otras publicaciones'))
    )

    permission = models.PositiveIntegerField(_('opción'), choices=PERMISSION_CHOICES)

    def __str__(self):
        return self.get_permission_display()

    class Meta:
        verbose_name = _('Permiso')
        verbose_name_plural = _('Permisos')


class UserBlogPermission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_permissions',
                             on_delete=models.CASCADE, verbose_name=_('usuario'))

    blog = models.ForeignKey('Blog', related_name='permissions',
                             verbose_name=_('blog'), on_delete=models.CASCADE)

    permissions = models.ManyToManyField(BlogPermission, related_name='permissions', verbose_name=_('permisos'))

    def __str__(self):
        return self.user.username
