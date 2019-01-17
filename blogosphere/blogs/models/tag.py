from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from ...mixins.models.admin import AdminURLMixin


class Tag(models.Model, AdminURLMixin):
    name = models.CharField(_('nombre'),
                            unique=True,
                            max_length=255)

    class Meta:
        verbose_name = _('Etiqueta')
        verbose_name_plural = _('Etiquetas')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = slugify(self.name).replace('-', ' ')
        super(Tag, self).save(*args, **kwargs)
