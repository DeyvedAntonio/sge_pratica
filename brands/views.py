from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
)
from django.urls import reverse_lazy
from .forms import BrandForm
from .models import Brand


class BrandListView(ListView):

    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'


class BrandCreateView(CreateView):

    model = Brand
    form_class = BrandForm
    template_name = 'brand_create.html'
    success_url = reverse_lazy('brand-list')


class BrandDetailView(DetailView):

    model = Brand
    template_name = 'brand_detail.html'


class BrandUpdateView(UpdateView):

    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand-list')
