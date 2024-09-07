from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
