from django.db import models
import uuid
from django.conf import settings

# Create your models here.

class DeliveryOptions(models.Model):
    """
    The Delivery methods table contining all delivery
    """

    DELIVERY_CHOICES = [

        ("DD", "Digital Delivery")
    ]

    delivery_name = models.CharField(
        verbose_name=("delivery_name"),
        help_text=("Required"),
        max_length=255,
    )
    delivery_price = models.DecimalField(
        verbose_name=("delivery price"),
        help_text=("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": ("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
        default=0.00,
    )
    delivery_method = models.CharField(
        choices=DELIVERY_CHOICES,
        verbose_name=("delivery_method"),
        help_text=("Required"),
        max_length=255,
        default = False,
    )

    order = models.IntegerField(verbose_name=("list order"), help_text=("Required"), default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Delivery Option")
        verbose_name_plural = ("Delivery Options")

    def __str__(self):
        return self.delivery_name

class PaymentSelections(models.Model):
    """
    Store payment options
    """

    name = models.CharField(
        verbose_name=("name"),
        help_text=("Required"),
        max_length=255,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Payment Selection")
        verbose_name_plural = ("Payment Selections")

    def __str__(self):
        return self.name
    
class MockOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    
    
    

