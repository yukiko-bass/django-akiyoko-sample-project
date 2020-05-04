from django.shortcuts import render
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
