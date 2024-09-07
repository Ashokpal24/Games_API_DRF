from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Publisher
from .serializer import PublisherSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [AllowAny]
