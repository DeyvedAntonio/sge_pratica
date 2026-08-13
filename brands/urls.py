from django.urls import path
from .views import BrandListView, BrandCreateView


urlpatterns = [
    path('list/', BrandListView.as_view(), name='brand-list'),
    path('create/', BrandCreateView.as_view(), name='brand-create'),
]
