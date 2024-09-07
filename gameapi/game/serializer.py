from .models import Game
from rest_framework import serializers


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "url", "name", "release_year",
                  "description", "publisher", "developer", "price"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request and request.method == 'GET':
            representation.pop('price', None)
        return representation
