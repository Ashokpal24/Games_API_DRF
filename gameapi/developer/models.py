from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_founding = models.DateField()

    def __str__(self):
        return self.name
