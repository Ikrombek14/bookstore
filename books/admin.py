from django.contrib import admin

# Register your models here.
from .models import Books_category, Authors, Books, Review

admin.site.register(Books_category)
admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Review)
