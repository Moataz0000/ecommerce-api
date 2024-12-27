import uuid

from django.db import models
from users.models import User
from products.models import Product




class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'PG', 'Pending'
        CONFIRMED = 'CF', 'Confirmed'
        SHIPPED  = 'SP', 'Shipped'
        DELIVERD = 'DV', 'Deliverd'
        CANCELLED = 'CL', 'Cancelled'

    order_id = models.CharField(unique=True, max_length=8, editable=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.order_id} by {self.user.email}'

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4().int)[:8]
        super().save(*args, **kwargs)