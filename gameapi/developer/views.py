from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Developer
from .serializer import DeveloperSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [AllowAny]
