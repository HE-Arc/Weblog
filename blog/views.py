from django.shortcuts import render
from django.utils import timezone
from .models import Article, Comment
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
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Index(ListView):
    template_name = 'blog/base_index.html'
    model = Article
    ordering = ['-date']
    paginate_by = 10


class ArticleView(View):

    def get(self, request, slug):
        # Tri les articles selon la date de publication
        articles_full_list = Article.objects.order_by('-date')
        i = 0
        # récupération de la position dans la liste
        for article in articles_full_list:
            i += 1
            if article.slug == slug:
                # très très sale
                index = i-1
        previous_slug = None
        next_slug = None
        article = articles_full_list[index]
        if index > 0:
            previous_slug = articles_full_list[index-1].slug
        if index < len(articles_full_list)-1:    
            next_slug = articles_full_list[index+1].slug
        
        #Récupère tous les commentaires
        comments_full_list = Comment.objects.order_by('-date')
        comments_article_list = None
        for comment in comments_full_list:
            if comment.article == article.slug: 
                comments_article_list.add(comment)
        return render(request, 'blog/base_article.html', {'article': article, 'user': self.request.user.pk, 'previous_slug': previous_slug, 'next_slug': next_slug, 'comments': comments_article_list})
    
	
    

class ArticleNewForm(LoginRequiredMixin ,CreateView):
    # def get(self, request):
    #     if request.user.is_authenticated:

    model = Article

    # derp = forms.CharField(widget=MarkdownWidget())
    fields = ["title", "body"]
    success_url = '/weblog/'
    redirect_field_name = '/weblog/'


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

class Search(ListView):
    template_name = 'blog/base_index.html'
		
    #Récupère tous les articles
    comments_full_list = Comment.objects.order_by('-date')
    articles_list = None
    for comment in comments_full_list:
        if comment.article == article.slug: 
            comments_article_list.add(comment)

	
def request_page(request):
    if(request.GET.get('search_button')):
        print("test")    
    return render(request,'blog/result_search.html')