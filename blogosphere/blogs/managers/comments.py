from modeltranslation.manager import MultilingualQuerySet
from . import PUBLISHED


class CommentsSet(MultilingualQuerySet):
    def published(self):
        comments = self.filter(status=PUBLISHED)
        return comments
