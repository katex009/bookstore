from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    login_url = '/accounts/login' 

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'