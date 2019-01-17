from django import forms
from django.utils.translation import ugettext_lazy as _

from dal import autocomplete

from ...models import UserBlogPermission


class UserBlogForm(forms.ModelForm):
    class Meta:
        model = UserBlogPermission
        fields = forms.ALL_FIELDS

        widgets = {

            'blog': autocomplete.ModelSelect2(url='blogs:autocompletes:blog_autocomplete',
                                              attrs={'data-placeholder': _('Blog...'),
                                                     }),

        }
