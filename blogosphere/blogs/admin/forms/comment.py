from django import forms
from django.utils.translation import ugettext_lazy as _
from django_comments.forms import CommentSecurityForm, COMMENT_MAX_LENGTH
from versatileimagefield.fields import SizedImageCenterpointClickDjangoAdminField

from dal import autocomplete

from ...models import Comment


class CommentForm(forms.ModelForm):
    # name = forms.CharField(label=_('Nombre...'), max_length=50, required=False)
    # email = forms.EmailField(label=_("Correo..."), required=False)
    #
    # comment = forms.CharField(label=_('Comentario...'), widget=forms.Textarea,
    #                           max_length=COMMENT_MAX_LENGTH)


    class Meta:
        model = Comment
        fields = forms.ALL_FIELDS
        widgets = {
            'post': autocomplete.ModelSelect2(url='blogs:autocompletes:post_autocomplete',
                                              attrs={
                                                  'data-placeholder': _('Publicación...'),
                                              }),
        }
