from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey

from ...mixins.models.admin import AdminURLMixin


class Category(MPTTModel, AdminURLMixin):
    """"
    Model in order to categorizing posts
    """
    # region fields

    title = models.CharField(_('título'), max_length=255)

    slug = models.SlugField(
        _('slug'), unique=True, max_length=255,
        help_text=_("Used to build the category's URL."))

    description = models.TextField(
        _('descripción'), blank=True)

    parent = TreeForeignKey('self', related_name='children',
                            null=True, blank=True,
                            on_delete=models.SET_NULL,
                            verbose_name=_('categoría padre'))


    # endregion

    # region properties
    @property
    def tree_path(self):
        """
        Returns category's tree path
        by concatening the slug of his ancestors.
        """
        if self.parent_id:
            return '/'.join(
                [ancestor.slug for ancestor in self.get_ancestors()] +
                [self.slug])
        return self.slug

    # endregion

    # region custom methods

    def __str__(self):
        return self.title

    # endregion

    class Meta:
        """
        Category's meta informations.
        """
        ordering = ['title']
        unique_together = ('parent', 'slug')
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorías')
        permissions = (('can_manage_categories', _('Puede gestionar categorías')),
                       )

    class MPTTMeta:
        """
        Category MPTT's meta informations.
        """
        order_insertion_by = ['title']
