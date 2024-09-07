from .models import Developer
from rest_framework import serializers


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ["id", "url", "name", "description", "date_of_founding"]
