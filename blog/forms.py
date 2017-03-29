from django import forms
from .models import Article


class PostArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']
