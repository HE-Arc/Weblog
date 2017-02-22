from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=134)
    date = models.DateField()
    body = models.CharField()
    # category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # author=models.ForeignKey(Author,on_delete=models.CASCADE)
    # tags=models.ForeignKey(Tag,on_delete=models.CASCADE)# usefull?
    slug = models.AutoField(primary_key=True)
