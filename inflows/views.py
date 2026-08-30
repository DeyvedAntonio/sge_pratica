from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)
from django.urls import reverse_lazy
from .forms import InflowForm
from .models import Inflow


class InflowCreateView(CreateView):

    model = Inflow
    template_name = 'inflow_create.html'
    success_url = reverse_lazy('inflow-list')
    form_class = InflowForm


class InflowDetailView(DetailView):

    model = Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflows'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class InflowListView(ListView):

    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
