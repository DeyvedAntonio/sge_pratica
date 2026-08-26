from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
)

app_name = 'category'

urlpatterns = [
    path(
        'list/',
        CategoryListView.as_view(),
        name='category-list',
    ),
    path(
        'create/',
        CategoryCreateView.as_view(),
        name='category-create',
    ),
    path(
        '<str:uuid>/delete/',
        CategoryDeleteView.as_view(),
        name='category-delete',
    ),
    path(
        '<str:uuid>/detail/',
        CategoryDetailView.as_view(),
        name='category-detail',
    ),
    path(
        '<str:uuid>/update/',
        CategoryUpdateView.as_view(),
        name='category-update',
    ),
]