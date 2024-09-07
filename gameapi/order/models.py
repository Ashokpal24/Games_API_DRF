from django.db import models
from user.models import User
from game.models import Game


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(
        max_digits=8, decimal_places=2, editable=False)

    def __str__(self):
        return f"Order for {self.game.name} by {self.user.name}"
