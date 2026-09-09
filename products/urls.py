from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product-list'),
    path('<str:uuid>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('<str:uuid>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('<str:uuid>/detail/', views.ProductDetailView.as_view(), name='product-detail'),
]