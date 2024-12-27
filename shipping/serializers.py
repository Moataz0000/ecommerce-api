from rest_framework import serializers
from .models import CartItem, Cart
from products.models import Product
from .models import ShippingAddress

class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')


    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'total_price']



class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()


    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()



class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country', 'phone']