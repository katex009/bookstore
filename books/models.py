from django.db import models
from django.urls import reverse
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])