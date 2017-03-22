from django.shortcuts import render
from django.utils import timezone
from .models import Article
from .models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
# from .forms import AuthForm
from django.contrib.auth import authenticate, login


# Create your views here.
class Index(View):
    def get(self, request):
        # Tri les articles selon la date de publication
        articles = Article.objects.filter(date__lte=timezone.now()).order_by('date')
        user = User.objects
        return render(request, 'blog/base.html', {'articles': articles, 'user': user})


# class AdminAuth(View):
#     def get(self, request):
#         form = AuthForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#         else:
#             form = AuthForm()
#
#         return render(request, 'blog/login.html', {'form': form})

class AuthView(View):
    def get(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            articles = Article.objects.filter(date__lte=timezone.now()).order_by('date')
            return render(request, 'blog/index.html', {'articles': articles})
