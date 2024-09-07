from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "url", "user", "game", "price"]


class OrderListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "url", "user", "game", "price", "discount"]
