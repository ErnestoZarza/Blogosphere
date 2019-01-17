from django.db import models


class AdminURLMixin(object):
    @models.permalink
    def get_admin_url(self):
        return 'admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), (self.id,)
