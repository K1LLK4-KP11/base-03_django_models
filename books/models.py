from django.db import models

STATUS_CHOICES = [
('D', 'Черновик'),
('P', 'Опубликовано'),
]
status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D')  

# Create your models here.


class Author(models.Model):  
    name = models.CharField(max_length=100)  
    bio = models.TextField(max_length=500)
    birth_date = models.DateTimeField

GENRE_CHOICES = [
('literature', 'художественная литература'),
('non-fiction', 'Нон-фикшн'),
('sci-fi', 'научная фантастика'),
]

class Genre(models.Model):
    name = models.CharField(choices=GENRE_CHOICES)


class Book(models.Model):  
    title = models.CharField(max_length=100)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.BooleanField(default=False)
    published_date = models.DateTimeField  
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def is_available(self):  
        self.is_checked_out = True  
        return self.is_checked_out
