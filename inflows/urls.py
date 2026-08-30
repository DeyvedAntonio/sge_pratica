from django.urls import path
from . import views


urlpatterns = [
    path(
        'list/',
        views.InflowListView.as_view(),
        name='inflow-list',
    ),
    path(
        '<str:uuid>/detail/',
        views.InflowDetailView.as_view(),
        name='inflow-detail',
    ),
    path(
        'create/',
        views.InflowCreateView.as_view(),
        name='inflow-create',
    ),
]
