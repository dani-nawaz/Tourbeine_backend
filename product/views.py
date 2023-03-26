from django.core.exceptions import PermissionDenied
from rest_framework import generics, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from product.models import Category
from .models import Product, ProductBookmark
from .serializers import ProductSerializer, ProductBookmarkSerializer, CategorySerializer


class ListCreateCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RetrieveUpdateDestroyCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCreateProduct(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs.get('category'):
            return Product.objects.filter(category=self.kwargs['category'])
        return Product.objects.all()


class RetrieveUpdateDestroyProduct(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductSerializer


class ProductBookmarkListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductBookmarkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return ProductBookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductBookmarkRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductBookmark.objects.all()
    serializer_class = ProductBookmarkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You don't have permission to access this bookmark.")
        return obj


class UserSavedProductsListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        bookmarked_products = ProductBookmark.objects.filter(user=self.request.user).values_list('product_id',
                                                                                                 flat=True)
        return Product.objects.filter(pk__in=bookmarked_products)
