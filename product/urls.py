from django.urls import path

from . import views

urlpatterns = [
    path("category/", views.ListCreateCategory.as_view()),
    path("category/<int:pk>/", views.RetrieveUpdateDestroyCategory.as_view()),

    path("all/", views.ListCreateProduct.as_view()),
    path("<int:pk>/", views.RetrieveUpdateDestroyProduct.as_view()),
]

urlpatterns += [
    path('product-bookmarks/', views.ProductBookmarkListCreateView.as_view(), name='product-bookmark-list-create'),
    path('product-bookmarks/<int:pk>/', views.ProductBookmarkRetrieveUpdateDeleteView.as_view(),
         name='product-bookmark-retrieve-update-delete'),
    path('user-saved-products/', views.UserSavedProductsListView.as_view(), name='user-saved-products-list'),
]
