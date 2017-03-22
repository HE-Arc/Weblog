from django.conf.urls import url, include
from blog.views import Index, PostArticleForm
from . import views

urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^newArticle/$', PostArticleForm.as_view()),
    url('^', include('django.contrib.auth.urls')),
]
