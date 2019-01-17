from django.db.models import QuerySet

from mptt.managers import TreeQuerySet

from . import DRAFT, HIDDEN, PUBLISHED


class StatusSet(QuerySet):

    def published(self):
        return self.filter(status=PUBLISHED)

    def draft(self):
        return self.filter(status=DRAFT)

    def hidden(self):
        return self.filter(status=HIDDEN)


class TreeSet(TreeQuerySet):

    def first_level(self):
        return self.filter(level__lte=0)

    def published(self):
        return self.filter(status=PUBLISHED)

    def draft(self):
        return self.filter(status=DRAFT)

    def hidden(self):
        return self.filter(status=HIDDEN)
