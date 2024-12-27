from django.db import models
from django.conf import settings

from orders.models import Order
from products.models import Product




class Cart(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart for {self.owner.first_name} {self.owner.last_name}'

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def total_price(self):
        return self.product.price * self.quantity





class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shipping_addresses')
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_address')
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)



    def __str__(self):
        return f'Shipping Address for order #{self.order.id}'



