from django.conf.urls import url, include
from blog.views import Index, ArticleNewForm
from . import views

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^newArticle/$', ArticleNewForm.as_view()),
    url('^', include('django.contrib.auth.urls')),
    url('^markdownx/', include('markdownx.urls')),
]
