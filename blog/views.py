from django.shortcuts import render
from django.utils import timezone
from .models import Article
from .models import User
from django.http import HttpResponse
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request):
        # Tri les articles selon la date de publication
        articles = Article.objects.filter(date__lte=timezone.now()).order_by('date')
        user = User.objects
        return render(request, 'blog/base.html', {'articles': articles, 'user': user})


