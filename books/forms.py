from django.forms import ModelForm
from .models import Books


class BooksForm(ModelForm):
    model = Books
    fields = '__all__'