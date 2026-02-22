from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product


class RecipeListView(ListView):
    model = Product
    template_name = "pending.html"


class RecipeDetailView(DetailView):
    model = Product
    template_name = "pending.html"


# Create your views here.
