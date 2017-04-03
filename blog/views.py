from django.shortcuts import render
from django.utils import timezone
from .models import Article
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
        return render(request, 'blog/base.html', {'articles': articles, 'user': self.request.user.pk})


class ArticleNewForm(CreateView):
    model = Article
    fields = ["title", "body"]

    # TODO: succes url
    success_url = '/weblog/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        form.instance.date = timezone.now()
        form.instance.slug = form.instance.title

        return super().form_valid(form)


# ##DEPRECATED
# class PostTest(View):
#     def post(self, request):
#         if request.method == 'POST':
#             form = PostArticleForm(request.POST)
#             if form.is_valid():
#                 # post = form.save(commit=False)
#                 # post.author = request.user
#                 # post.published_date = timezone.now()
#                 # post.save()
#                 # print("~~~~~~~~~~~~~~~~~~DEBUG~~~~~~~~~~~~")
#                 # print(request.user.name)
#                 # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
#
#                 # curUser = User.objects.get(self.request.user)
#                 #
#                 # article = Article(author=curUser, title=title, body=body)
#                 # article.save()
#                 return HttpResponseRedirect('index')
#         else:
#             form = PostArticleForm()
#
#         return render(request, 'blog/article_form.html', {'form': form})
#
#     def get(self, request):
#         form = PostArticleForm()
#
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
