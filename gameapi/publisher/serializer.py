from rest_framework import serializers
from .models import Publisher


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "url", "name", "description", "date_of_founding"]
