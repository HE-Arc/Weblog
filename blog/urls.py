from django.conf.urls import url, include
from blog.views import Index, ArticleNewForm, PostTest
from . import views

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^newArticle/$', ArticleNewForm.as_view()),
    url(r'^testPost/$', PostTest.as_view(), name='testpost'),
    url('^', include('django.contrib.auth.urls')),
]
