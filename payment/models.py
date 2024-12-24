from django.db import models
from orders.models import Order




class Payment(models.Model):
    CREDIT_CARD = 'credit_card'
    PAYPAL = 'paypal'
    APPLE_PAY = 'apple_pay'

    PAYMENT_METHODS = [
        (CREDIT_CARD, 'Credit Card'),
        (PAYPAL, 'PayPal'),
        (APPLE_PAY, 'Apple Pay')
    ]

    class PaymentStatus(models.TextChoices):
        PENDING = 'PG', 'Pending'
        COMPLETED = 'CP', ('Compeleted'
                           '')
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment for Order {self.order.order_id}'