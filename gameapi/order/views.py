from rest_framework import viewsets
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin
)
from rest_framework.permissions import AllowAny
from .models import Order
from .serializer import (OrderSerializer, OrderListSerializer)


class OrderPostViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class OrderListViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [AllowAny]
