from django import forms
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from dal import autocomplete

from ...models import Author
from ..widgets import MiniTextArea


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = forms.ALL_FIELDS
        widgets = {
            'description_es': CKEditorUploadingWidget,
            'description_en': CKEditorUploadingWidget,
            'description_fr': CKEditorUploadingWidget,
        }