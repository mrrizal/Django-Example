from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_ajax.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^more/$', views.more_todo, name='more'),
  	url(r'^add/$', views.add_todo, name='add'),
]
