from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm
from brands.models import Brand
from categories.models import Category


class ProductCreateView(CreateView):

    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):

    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product-list')


class ProductDetailView(DetailView):

    model = Product
    template_name = 'product_detail.html'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class ProductUpdateView(UpdateView):

    model = Product
    template_name = 'product_update.html'
    success_url = reverse_lazy('product-list')
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class ProductListView(ListView):

    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context
