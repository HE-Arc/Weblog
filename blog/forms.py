from django import forms
from .models import Article

class PostArticleForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
