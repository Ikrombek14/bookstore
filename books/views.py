from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.views import View, generic
from django.views.generic import UpdateView, CreateView

from . import forms
# Create your views here.
from .models import Books


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def log_out(request):
    logout(request)
    return redirect('login_page')


def login_page(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'login.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "registration.html"


@login_required_decorator
def home_page(request):
    books = Books.objects.all()
    return render(request, 'index.html', {'books': books})


@login_required_decorator
def book_detail(request, pk):
    book = Books.objects.get(pk=pk)
    return render(request, 'detail.html', {'book': book})


class CreateBookView(CreateView):
    model = Books
    fields = '__all__'
    template_name = 'add_book.html'

    success_url = reverse_lazy('home_page')


@login_required_decorator
def delete_book(request, pk):
    book = Books.objects.get(pk=pk)
    book.delete()
    return redirect('home_page')


class UpdateBookView(UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'update_book.html'
    success_url = reverse_lazy('home_page')
    context_object_name = 'book'
