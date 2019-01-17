import os
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.placeholder import OnDiscPlaceholderImage
from versatileimagefield.registry import versatileimagefield_registry
from versatileimagefield.versatileimagefield import CroppedImage, ThumbnailImage


class CustomThumbnailImage(ThumbnailImage):
    def process_image(self, image, image_format, save_kwargs,
                      width, height):
        save_kwargs['icc_profile'] = None
        return super(CustomThumbnailImage, self).process_image(image, image_format, save_kwargs, width, height)


class CustomCroppedImage(CroppedImage):
    def process_image(self, image, image_format, save_kwargs,
                      width, height):
        save_kwargs['icc_profile'] = None
        return super(CustomCroppedImage, self).process_image(image, image_format, save_kwargs, width, height)


versatileimagefield_registry.unregister_sizer('thumbnail')
versatileimagefield_registry.register_sizer('thumbnail', CustomThumbnailImage)
versatileimagefield_registry.unregister_sizer('crop')
versatileimagefield_registry.register_sizer('crop', CustomCroppedImage)


def image_upload_to_dispatcher(instance, filename):
    """
    Dispatch function to allow overriding of ``image_upload_to`` method.
    Outside the model for fixing an issue with Django's migrations on Python 2.
    """
    return instance.image_upload_to(filename)


class ImageMixin(models.Model):
    def image_upload_to(self, filename):
        """
        Compute the upload path for the image field.
        """
        filename, ext = os.path.splitext(filename)

        return os.path.join(
            settings.UPLOAD_TO,
            self._meta.app_label,
            self._meta.model_name,
            '%s%s' % (slugify(filename), ext)
        )

    height = models.PositiveIntegerField(
        _('ancho de la imagen'),
        default=100,
        blank=True,
        null=True
    )

    width = models.PositiveIntegerField(
        _('alto de la imagen'),
        default=100,
        blank=True,
        null=True
    )

    ppoi = PPOIField(
        _('Punto primario de Interés (PPOI)'),
    )

    image = VersatileImageField(
        _('imagen principal'), blank=True,
        upload_to=image_upload_to_dispatcher, max_length=255,
        width_field='width',
        height_field='height',
        ppoi_field='ppoi',
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.MEDIA_ROOT, 'default',
                'no-image-icon-400x400.png'
            )
        ),
        help_text=_('Usado para ilustración.'))

    image_caption = models.TextField(
        _('leyenda'), blank=True, null=True,
        help_text=_('Leyenda de la imagen.'))

    class Meta:
        abstract = True


class BannerMixin(models.Model):
    def banner_image_upload_to(self, filename):
        """
        Compute the upload path for the image field.
        """
        filename, ext = os.path.splitext(filename)

        return os.path.join(
            settings.UPLOAD_TO,
            self._meta.app_label,
            self._meta.model_name,
            '%s%s' % (slugify(filename), ext)
        )

    banner_height = models.PositiveIntegerField(
        _('ancho de la imagen'),
        default=100,
        blank=True,
        null=True
    )

    banner_width = models.PositiveIntegerField(
        _('alto de la imagen'),
        default=100,
        blank=True,
        null=True
    )

    banner_ppoi = PPOIField(
        _('Punto primario de Interés (PPOI)'),
    )

    banner_image = VersatileImageField(
        _('banner del blog'), blank=True,
        upload_to=image_upload_to_dispatcher, max_length=255,
        width_field='banner_width',
        height_field='banner_height',
        ppoi_field='banner_ppoi',
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.MEDIA_ROOT, 'default',
                'no-image-icon-400x400.png'
            )
        ),
        help_text=_('Usado para ilustración.'))

    banner_image_caption = models.TextField(
        _('leyenda'), blank=True, null=True,
        help_text=_('Leyenda de la imagen.'))

    class Meta:
        abstract = True
