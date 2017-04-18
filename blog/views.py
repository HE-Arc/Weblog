from django.shortcuts import render
from django.utils import timezone
from .models import Article
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView
from .forms import PostArticleForm
from django.contrib.auth import authenticate, login
from django_markdown.widgets import MarkdownWidget
import markdown
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect


# Create your views here.
class Index(View):
    def get(self, request):
        # Tri les articles selon la date de publication
        articles_full_list = Article.objects.filter(date__lte=timezone.now()).order_by('-date')

        # Pagination
        page = request.GET.get('page', 1)
        paginator_index = Paginator(articles_full_list, 10)
        try:
            articles = paginator_index.page(page)
        except PageNotAnInteger:
            articles = paginator_index.page(1)
        except EmptyPage:
            articles = paginator_index.page(paginator_index.num_pages)
        return render(request, 'blog/base_index.html', {'articles': articles, 'user': self.request.user.pk})


class ArticleView(View):
    def get(self, request, slug):
        # Tri les articles selon la date de publication
        articles_full_list = Article.objects.filter(date__lte=timezone.now()).order_by('-date')

        i = 0
        # récupération de la position dans la liste
        for article in articles_full_list:
            i += 1
            if article.slug == slug:
                # très très sale
                index = i

        # Pagination
        page = request.GET.get('page', index)
        paginator_article = Paginator(articles_full_list, 1)
        try:
            articles = paginator_article.page(page)
        except PageNotAnInteger:
            articles = paginator_article.page(1)
        except EmptyPage:
            articles = paginator_article.page(paginator_article.num_pages)
        return render(request, 'blog/base_article.html', {'articles': articles, 'user': self.request.user.pk})


class ArticleNewForm(CreateView):
    # def get(self, request):
    #     if request.user.is_authenticated:
            model = Article

            # derp = forms.CharField(widget=MarkdownWidget())
            fields = ["title", "body"]
            # TODO: succes url
            success_url = '/weblog/'

            def form_valid(self, form):
                form.instance.author_id = self.request.user.pk
                form.instance.date = timezone.now()
                form.instance.slug = form.instance.title

                return super().form_valid(form)
        # else:
        #     return redirect('/weblog/')


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
