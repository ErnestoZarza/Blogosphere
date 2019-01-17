from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BlogosphereConfig(AppConfig):
    """
    Config for Blogs application.
    """
    name = 'blogosphere.blogs'
    label = 'blogs'
    verbose_name = _('Blogosfera')

    # def ready(self):
    #     """
    #     Connect signals here ...
    #     """
    #     from .signals import connect_signals
    #
    #     connect_signals()
