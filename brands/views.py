from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'


class BrandCreateView(CreateView):

    class Meta:
        model = Brand
        template_name = 'brand_create.html'
        success_url = reverse_lazy('brand_list')
