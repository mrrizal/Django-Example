from django.conf.urls import include, url
from homepage import views

urlpatterns = [
	url(r'^login$', views.LoginView.as_view(), name="login"),
	url(r'^$', views.index, name="index"),
	url(r'^logout$', views.logout_view, name="logout"),
]
