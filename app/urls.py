from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("brands/", include("brands.urls")),
    path('categories/', include('categories.urls')),
    path('supliers/', include('supliers.urls')),
    path('outflows/', include('outflows.urls')),
    path('inflows/', include('inflows.urls')),
    path('products/', include('products.urls')),
]
