from django.db import models


# Create your models here.
class Books_category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Authors(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name


class Books(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Books_category, on_delete=models.CASCADE)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    book_name = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

