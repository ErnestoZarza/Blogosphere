from django import forms
from django.utils.translation import ugettext_lazy as _

from dal import autocomplete

from ..widgets import MiniTextArea
from ...models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = forms.ALL_FIELDS
        widgets = {
            'description_es': MiniTextArea,
            'description_en': MiniTextArea,
            'description_fr': MiniTextArea,

            'image_caption_es': MiniTextArea,
            'image_caption_en': MiniTextArea,
            'image_caption_fr': MiniTextArea,

            'authors': autocomplete.ModelSelect2Multiple(url='blogs:autocompletes:author_autocomplete',
                                                attrs={
                                                    'data-placeholder': _('Autor...'),
                                                }),
        }