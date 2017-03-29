from django.shortcuts import render
from django.utils import timezone
from .models import Article, User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView
from .forms import PostArticleForm
from django.contrib.auth import authenticate, login


# Create your views here.
class Index(View):
    def get(self, request):
        # Tri les articles selon la date de publication
        articles = Article.objects.filter(date__lte=timezone.now()).order_by('date')
        user = User.objects
        return render(request, 'blog/base.html', {'articles': articles, 'user': user})


class ArticleNewForm(CreateView):
    model = Article
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        # ...
        return super(ArticleNewForm, self).form_valid(form)


# class PostArticleForm(View):
#     def get(self, request):
#         form = PostArticleForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#
#     def post(self, request):
#         form = PostArticleForm()
#         return render(request, 'blog/article_form.html', {'form': form})


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
