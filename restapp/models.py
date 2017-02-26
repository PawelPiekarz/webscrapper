from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True, unique=True)
    text = models.TextField()