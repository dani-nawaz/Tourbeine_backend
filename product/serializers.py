from rest_framework import serializers

from product.models import Category, Product, ProductBookmark


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductBookmarkSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductBookmark
        fields = '__all__'

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Product.objects.get(pk=product_data['id'])
        bookmark = ProductBookmark.objects.create(product=product, **validated_data)
        return bookmark
