from django.db import models
from django.db.models import permalink


# Create your models here.
class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    # infos: stuff about user
    infos = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=134)
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
    categories = models.ManyToManyField('Category')
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    slug = models.SlugField(primary_key=True)
	
    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_article_post', None, {'slug': self.slug})


class Comment(models.Model):
    author = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    email = models.EmailField()
    date = models.DateField(True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    # def __str__(self):
    #     return (self.email + self.date)
