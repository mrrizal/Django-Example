from django.conf.urls import include, url
from karyawan import views

urlpatterns = [
	url(r'^$', views.profile, name="profile"),
	url(r'^ganti_foto/', views.ganti_foto, name="ganti_foto"),
]
