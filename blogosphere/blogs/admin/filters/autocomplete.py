from django import forms
from django.contrib.admin.filters import SimpleListFilter
from django.core.exceptions import ImproperlyConfigured
from django.forms.widgets import Media, MEDIA_TYPES

from dal import autocomplete


class AutocompleteFilter(SimpleListFilter):
    template = "dal_admin_filters/autocomplete-filter.html"
    param_name = ''
    queryset_filter = None
    autocomplete_url = ''
    widget_attrs = {}

    def queryset(self, request, queryset):
        raise NotImplementedError()

    def __init__(self, request, params, model, model_admin):
        self.parameter_name = self.param_name
        super(AutocompleteFilter, self).__init__(request, params, model, model_admin)

        self._add_media(model_admin)

        field = forms.ModelChoiceField(
            queryset=self.queryset_filter,
            widget=autocomplete.ModelSelect2(
                url=self.autocomplete_url,
            )
        )

        attrs = self.widget_attrs.copy()
        attrs['id'] = self.param_name

        self.rendered_widget = field.widget.render(
            name=self.parameter_name,
            value=self.used_parameters.get(self.parameter_name, ''),
            attrs=attrs
        )

    def _add_media(self, model_admin):

        if not hasattr(model_admin, 'Media'):
            raise ImproperlyConfigured('Add empty Media class to %s. Sorry about this bug.' % model_admin)

        def _get_media(obj):
            return Media(media=getattr(obj, 'Media', None))

        media = _get_media(model_admin) + _get_media(AutocompleteFilter) + _get_media(self)

        for name in MEDIA_TYPES:
            setattr(model_admin.Media, name, getattr(media, "_" + name))

    def has_output(self):
        return True

    def lookups(self, request, model_admin):
        return ()

    class Media:
        css = {
            'all': (
                'autocomplete_light/vendor/select2/dist/css/select2.css',
                'autocomplete_light/select2.css',
                'dal_admin_filters/css/autocomplete-fix.css'
            )
        }
        js = (
            'autocomplete_light/jquery.init.js',
            'autocomplete_light/autocomplete.init.js',
            'autocomplete_light/vendor/select2/dist/js/select2.full.js',
            'autocomplete_light/select2.js',
            'dal_admin_filters/js/querystring.js',
        )




