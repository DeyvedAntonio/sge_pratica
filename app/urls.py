from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("brands/", include("brands.urls")),
    path('categories/', include('category.urls')),
    path('supliers/', include('supliers.urls')),
]
