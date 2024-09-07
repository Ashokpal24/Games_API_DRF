from django.db import models
from publisher.models import Publisher
from developer.models import Developer


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    release_year = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
