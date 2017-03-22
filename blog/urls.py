
from django.conf.urls import url,include
from blog.views import Index
from . import views


urlpatterns = [
    url(r'^$', Index.as_view()),
    url('^', include('django.contrib.auth.urls')),
]
