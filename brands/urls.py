from django.urls import path
from .views import (
    BrandListView,
    BrandCreateView,
    BrandDetailView,
    BrandUpdateView,
)


urlpatterns = [
    path('list/', BrandListView.as_view(), name='brand-list'),
    path('create/', BrandCreateView.as_view(), name='brand-create'),
    path('<int:pk>/detail/', BrandDetailView.as_view(), name='brand-detail'),
    path('<int:pk>/update/', BrandUpdateView.as_view(), name='brand-update'),
]
