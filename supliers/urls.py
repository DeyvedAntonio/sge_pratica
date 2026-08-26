from django.urls import path
from .views import (
    SuplierCreateView,
    SuplierDeleteView,
    SuplierDetailView,
    SuplierListView,
    SuplierUpdateView,
)


app_name = 'suplier'

urlpatterns = [
    path(
        'create/',
        SuplierCreateView.as_view(),
        name='suplier-create',
    ),
    path(
        '<str:uuid>/delete/',
        SuplierDeleteView.as_view(),
        name='suplier-delete',
    ),
    path(
        '<str:uuid>/detail/',
        SuplierDetailView.as_view(),
        name='suplier-detail',
    ),
    path(
        'list/',
        SuplierListView.as_view(),
        name='suplier-list',
    ),
    path(
        '<str:uuid>/update/',
        SuplierUpdateView.as_view(),
        name='suplier-update',
    ),
]