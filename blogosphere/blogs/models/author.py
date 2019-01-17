from django.db import models
from django.utils.translation import ugettext_lazy as _
from ...mixins.models.image import ImageMixin
from ...mixins.models.admin import AdminURLMixin


class CoreAuthor(models.Model, AdminURLMixin):
    name = models.CharField(_('nombre'), max_length=255)

    nickname = models.CharField(_('sobrenombre'), max_length=255,
                                blank=True)

    email = models.EmailField(_('correo'), blank=True)

    description = models.TextField(_('descripción'), blank=True)

    date_birthday = models.DateField(_('fecha de nacimiento'), null=True,
                                     blank=True)

    date_death = models.DateField(_('fecha de defunción'), null=True,
                                  blank=True)

    slug = models.SlugField(_('slug'), max_length=255,
                            unique=True,
                            help_text=_("Used to build the author's URL."))

    featured = models.BooleanField(_('destacado'), default=False)

    # region custom methods
    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.nickname:
            return self.nickname

        return self.name

    # endregion

    class Meta:
        abstract = True
        verbose_name = _('Autor')
        verbose_name_plural = _('Autores')


class ImageAuthor(ImageMixin):
    """
    Abstract model class to add an autor's image.
    """

    class Meta:
        abstract = True


class Author(CoreAuthor, ImageAuthor):
    """'Model Author"""
