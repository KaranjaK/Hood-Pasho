from django.conf.urls import url, include
from django.urls import URLPattern
from . import views
from django.conf import settings

# Define app urls
urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^register/$', views.signup, name='signup'),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^all-hoods/$', views.hoods, name='hood'),
    url(r'^new-hood/$', views.create_hood, name='new-hood'),
]