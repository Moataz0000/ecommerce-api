from .models import Product, Category, Image
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'created']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['name', 'category', 'slug', 'description', 'price', 'stock', 'created']


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    category = serializers.CharField(write_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']

    def validate_category(self, value):
        """Convert the category name to a Category instance."""
        try:
            return Category.objects.get(name=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")

    def create(self, validated_data):
        category = validated_data.pop('category')
        return Product.objects.create(category=category, **validated_data)

    def update(self, instance, validated_data):
        category = validated_data.pop('category', None)
        if category:
            instance.category = category
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['product', 'image']
