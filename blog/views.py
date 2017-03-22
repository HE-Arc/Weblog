from django.shortcuts import render
from django.utils import timezone
from .models import Article


# Create your views here.
def index(request):
    # Tri les articles selon la date de publication
    articles = Article.objects.filter(date__lte=timezone.now()).order_by('date')

    return render(request, 'blog/index.html', {'articles': articles})
