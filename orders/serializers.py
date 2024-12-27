from .models import Order
from shipping.serializers import ShippingAddressSerializer
from rest_framework import serializers




class OrderSerializer(serializers.ModelSerializer):
    items = serializers.CharField(read_only=True)
    total_price = serializers.SerializerMethodField()
    shipping_address = ShippingAddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created', 'status', 'items', 'total_price', 'shipping_address']

    def get_total_price(self, obj):
        return obj.total_price()
