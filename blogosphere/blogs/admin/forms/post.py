from django import forms
from django.utils.translation import ugettext_lazy as _

from dal import autocomplete
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from ..widgets import MiniTextArea
from ...models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # model = Post
        fields = forms.ALL_FIELDS

        widgets = {
            'lead_es': CKEditorUploadingWidget(),
            'lead_en': CKEditorUploadingWidget(),
            'lead_fr': CKEditorUploadingWidget(),

            'excerpt_es': MiniTextArea,
            'excerpt_en': MiniTextArea,
            'excerpt_fr': MiniTextArea,

            'image_caption_es': MiniTextArea,
            'image_caption_en': MiniTextArea,
            'image_caption_fr': MiniTextArea,

            'body_es': CKEditorUploadingWidget(),
            'body_en': CKEditorUploadingWidget(),
            'body_fr': CKEditorUploadingWidget(),

            'blog': autocomplete.ModelSelect2(url='blogs:autocompletes:blog_autocomplete',
                                              attrs={'data-placeholder': _('Blog...'),
                                                     }),
            'source': autocomplete.ModelSelect2(url='blogs:autocompletes:source_autocomplete',
                                                attrs={'data-placeholder': _('Fuente ...'),
                                                       # 'data-minimum-input-length': 3,
                                                       }),
            'authors': autocomplete.ModelSelect2Multiple(url='blogs:autocompletes:author_autocomplete',
                                                         attrs={'data-placeholder': _('Autores ...'),
                                                                # 'data-minimum-input-length': 3,
                                                                }),
            'categories': autocomplete.ModelSelect2Multiple(url='blogs:autocompletes:category_autocomplete',
                                                            attrs={'data-placeholder': _('Categorías ...'),
                                                                   # 'data-minimum-input-length': 3,
                                                                   }),
            'related': autocomplete.ModelSelect2Multiple(url='blogs:autocompletes:post_autocomplete',
                                                         attrs={'data-placeholder': _('Publicaciones relacionadas ...'),
                                                                # 'data-minimum-input-length': 3,
                                                                }),
            'tags': autocomplete.ModelSelect2Multiple(url='blogs:autocompletes:tag_autocomplete',
                                                      attrs={'data-placeholder': _('Etiquetas...')}),

            'reference': autocomplete.ModelSelect2(url='blogs:autocompletes:post_autocomplete',
                                                   attrs={'data-placeholder': _('Referencia...'),
                                                          }),
        }
