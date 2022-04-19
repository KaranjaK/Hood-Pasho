from django.conf.urls import url, include
from django.urls import URLPattern
from . import views
from django.conf import settings

# Define app urls
urlpatterns = [
    url('^$', views.index, name='index'),
]