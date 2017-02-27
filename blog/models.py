from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

class User(models.Model):
    name = models.CharField(max_length=100)
    # infos: stuff about user
    infos = models.CharField(max_length=1000)

class Tag(models.Model):
    name = models.CharField(max_length=20)

class Article(models.Model):
    title = models.CharField(max_length=134)
    date = models.DateField()
    body = models.TextField()
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(primary_key=True)


class Comment(models.Model):
    author = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    email = models.EmailField()
    date = models.DateField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
