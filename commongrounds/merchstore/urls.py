from django.urls import path
from .views import MerchListView, MerchDetailView

app_name = "merchstore"
urlpatterns = [
    path("items/", MerchListView.as_view(), name="merch_list"),
    path("item/<int:pk>/", MerchDetailView.as_view(), name="merch_detail"),
]
