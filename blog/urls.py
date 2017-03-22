from django.conf.urls import url
from blog.views import Index
from . import views

urlpatterns = [
    url(r'^$', Index.as_view()),
]
