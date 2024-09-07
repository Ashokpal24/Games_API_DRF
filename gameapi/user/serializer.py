from rest_framework import serializers
from .models import User


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'name', "email", "url"]


class UserDetailedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'name', "email", "url", "address", "phone_number"]
