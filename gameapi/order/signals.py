from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order


@receiver(pre_save, sender=Order)
def update_discount(sender, instance, **kwargs):
    original_price = instance.game.price
    if instance.price < original_price:
        instance.discount = (
            (original_price-instance.price)/original_price)*100
    else:
        instance.discount = 0
