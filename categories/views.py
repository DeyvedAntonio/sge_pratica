from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Category
from .forms import CategoryForm


class CategoryCreateView(CreateView):

    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):

    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category:category-list')
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class CategoryDetailView(DetailView):

    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'categories'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class CategoryListView(ListView):

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryUpdateView(UpdateView):

    model = Category
    template_name = 'category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:category-list')
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
