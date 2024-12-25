from django.core.serializers import serialize
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ProductCreateUpdateSerializer
from .services import ProductManagement
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.select_related('owner', 'category').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'slug']
    ordering_fields = ['price', 'stock', 'created']


class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Pass the user to the service layer for ownership handling
        ProductManagement.create_product(serializer.validated_data, self.request.user)


class ProductDetialView(generics.RetrieveAPIView):
    queryset = Product.objects.select_related('owner', 'category').all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.select_related('owner', 'category').all()
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_update(self, serializer):
        product = self.get_object()
        ProductManagement.update_product(product, serializer.validated_data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Product updated successfully!"}, status=status.HTTP_200_OK)


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.select_related('owner', 'category').all()
    lookup_field = 'slug'

    def perform_destroy(self, instance):
        ProductManagement.delete_product(instance)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Product deleted successfully!"}, status=status.HTTP_200_OK)