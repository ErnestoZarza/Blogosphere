from django.conf import settings

from rest_framework import serializers
from urllib.parse import urljoin

from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField('absolute_url')

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url')
        ]
    )

    def absolute_url(self, obj):
        return urljoin(settings.SITE_DOMAIN, obj.get_absolute_url())

    class Meta:
        model = Post
        fields = (
            'title',
            'image',
            'url',
        )
