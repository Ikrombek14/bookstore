
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View, generic
# Create your views here.
from .models import Books

class ListView(View):

    def get(self, request):
        books = Books.objects.all()
        return render(request, 'index.html', {'books': books})


class BookDetailView(DetailView):

    model = Books
    template_name = 'detail.html'
    context_object_name = 'book'


class CreateBookView(CreateView):
    model = Books
    fields = '__all__'
    template_name = 'add_book.html'

    success_url = reverse_lazy('index')


class UpdateBookView(UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'update_book.html'
    success_url = reverse_lazy('index')
    context_object_name = 'book'


class DeleteBookView(DeleteView):
    model = Books
    template_name = 'delete_book.html'
    success_url = reverse_lazy('index')
    context_object_name = 'book'
