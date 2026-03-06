from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Commission


class CommissionListView(ListView):
    model = Commission
    template_name = "commission_list.html"


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commission_detail.html"
