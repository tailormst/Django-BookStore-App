from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title