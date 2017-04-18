from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.conf import settings
from autoslug import AutoSlugField
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


# Create your models here.
class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.name


#
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     # infos: stuff about user
#     infos = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.name



class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=134)
    date = models.DateField(auto_now_add=True)
    # body = models.TextField()
    body = MarkdownxField()

    categories = models.ManyToManyField('Category')
    # author = models.ForeignKey('User', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField('Tag')
    slug = AutoSlugField(populate_from='title', primary_key=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    def publish(self):
        # self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return title

    # @permalink
    def get_absolute_url(self):
        # return ('index')
        return reverse('index', args=[str(self.id)])

        # @property
        # def formatted_markdown(self):
        #     return markdownify(self.body)


class Comment(models.Model):
    author = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        # return (self.email + self.date)
        return (self.content)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        # return ('index')
        return reverse('index', args=[str(self.id)])

    def publish(self):
        # self.date = timezone.now()
        self.save()
