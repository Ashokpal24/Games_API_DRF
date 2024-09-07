from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Game
from .serializer import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]
