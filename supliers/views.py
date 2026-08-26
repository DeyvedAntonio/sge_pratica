from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import SuplierForm
from .models import Suplier


class SuplierCreateView(CreateView):

    model = Suplier
    template_name = 'suplier_create.html'
    success_url = reverse_lazy('suplier:suplier-list')
    form_class = SuplierForm


class SuplierDeleteView(DeleteView):

    model = Suplier
    template_name = 'suplier_delete.html'
    success_url = reverse_lazy('suplier:suplier-list')
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class SuplierDetailView(DetailView):

    model = Suplier
    template_name = 'suplier_detail.html'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class SuplierListView(ListView):

    model = Suplier
    template_name = 'suplier_list.html'
    context_object_name = 'supliers'


class SuplierUpdateView(UpdateView):

    model = Suplier
    template_name = 'suplier_update.html'
    form_class = SuplierForm
    success_url = reverse_lazy('suplier:suplier-list')
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
