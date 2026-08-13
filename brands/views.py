from django.views.generic import ListView
from .models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
