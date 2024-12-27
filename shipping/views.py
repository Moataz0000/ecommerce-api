from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Cart, CartItem
from products.models import Product
from .serializers import CartSerializer, CartItemSerializer
from orders.models import Order
from orders.serializers import OrderSerializer
from .models import ShippingAddress
from .serializers import ShippingAddressSerializer



class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(owner=self.request.user)
        return cart



class CartItemAddView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(owner=self.request.user)
        serializer.save(cart=cart)


class CartItemUpdateView(generics.UpdateAPIView):
    queryset = CartItem.objects.select_related('cart', 'product').all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]


class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.select_related('cart', 'product').all()
    permission_classes = [IsAuthenticated]




class ShippingAddressCreateView(generics.CreateAPIView):
    serializer_class = ShippingAddressSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        order = Order.objects.get(id=request.data.get("order_id"), user=request.user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, order=order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        status = request.data.get("status")
        if status not in dict(Order.OrderStatus):
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        order.status = status
        order.save()
        return Response(OrderSerializer(order).data)
