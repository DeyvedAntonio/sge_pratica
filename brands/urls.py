from django.urls import path
from .views import (
    BrandListView,
    BrandCreateView,
    BrandDetailView,
    BrandUpdateView,
    BrandDeleteView,
)


app_name = 'brand'

urlpatterns = [
    path('list/', BrandListView.as_view(), name='brand-list'),
    path('create/', BrandCreateView.as_view(), name='brand-create'),
    path(
        '<str:uuid>/detail/',
        BrandDetailView.as_view(),
        name='brand-detail',
    ),
    path(
        '<str:uuid>/update/',
        BrandUpdateView.as_view(),
        name='brand-update',
    ),
    path(
        '<str:uuid>/delete/',
        BrandDeleteView.as_view(),
        name='brand-delete',
    )
]
