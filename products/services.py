# services.py
from .models import Product

class ProductManagement:
    @staticmethod
    def create_product(validated_data, user):
        """Create a product and associate it with the given user."""
        category = validated_data.pop('category')  # Extract category instance
        return Product.objects.create(owner=user, category=category, **validated_data)

    @staticmethod
    def update_product(product, validated_data):
        """Update an existing product."""
        category = validated_data.pop('category', None)
        if category:
            product.category = category
        for attr, value in validated_data.items():
            setattr(product, attr, value)
        product.save()
        return product

    @staticmethod
    def delete_product(product):
        """Delete a product."""
        product.delete()
