from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .models import Outflow
from .forms import OutflowForm


class OutflowListView(ListView):

    model = Outflow
    paginate_by = 10
    context_object_name = 'outflows'


class OutflowCreateView(CreateView):

    model = Outflow
    form_class = OutflowForm
    success_url = reverse_lazy('outflow-list')


class OutflowDetailView(DetailView):

    model = Outflow
    context_object_name = 'outflows'
