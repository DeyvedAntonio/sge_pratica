from django.urls import path
from . import views


app_name = 'outflow'

urlpatterns = [
    path('list/', views.OutflowListView.as_view(), name='outflow-list'),
    path('<str:uuid>/detail/', views.OutflowDetailView.as_view(), name='outflow-detail'),
    path('create/', views.OutflowCreateView.as_view(), name='outflow-create'),
]
