from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from products.models import Product
from .serializers import CartSerializer, CartItemSerializer




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
