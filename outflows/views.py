from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .models import Outflow
from .forms import OutflowForm


class OutflowListView(ListView):

    model = Outflow
    template_name = 'outflow_list.html'
    paginate_by = 10
    context_object_name = 'outflows'


class OutflowCreateView(CreateView):

    model = Outflow
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow-list')


class OutflowDetailView(DetailView):

    model = Outflow
    template_name = 'outflow_detail.html'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
