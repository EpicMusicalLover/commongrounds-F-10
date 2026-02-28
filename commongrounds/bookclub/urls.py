from django.urls import path
from . import views BookListView, BookDetailView


app_name = "bookclub"


urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
