from django.conf.urls import url, include
from blog.views import Index, ArticleNewForm, ArticleView
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^newArticle/$', ArticleNewForm.as_view()),
    url('^', include('django.contrib.auth.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
	url(r'^article/(?P<slug>[\w-]+)/$', ArticleView.as_view()),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
