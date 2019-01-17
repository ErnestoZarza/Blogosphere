from django import forms
from django.utils.translation import ugettext_lazy as _

from dal import autocomplete

from ..widgets import MiniTextArea
from ...models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = forms.ALL_FIELDS
        widgets = {
            'description': MiniTextArea,

            'parent': autocomplete.ModelSelect2(url='blogs:autocompletes:category_autocomplete',
                                                attrs={
                                                    'data-placeholder': _('Categoría padre...'),
                                                }),
        }
