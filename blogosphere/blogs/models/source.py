from django.db import models
from django.utils.translation import ugettext_lazy as _


class Source(models.Model):
    name = models.CharField(_('nombre'), max_length=255)

    slug = models.SlugField(
        _('slug'), max_length=255,
        unique=True,
        help_text=_("Usado para construir la URL de la fuente."))

    url = models.URLField(_('url'), null=True, blank=True)

    class Meta:
        verbose_name = _('Fuente')
        verbose_name_plural = _('Fuentes')

    def __str__(self):
        return self.name