from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from kehadiran import views

urlpatterns = [
	url(r'^$', login_required(views.KehadiranView.as_view()), name="index"),
	url(r'^/pengajuan_izin$', views.pengajuan_izin, name="pengajuan_izin"),
	url(r'^/daftar_izin$', views.daftar_izin, name="daftar_izin"),
	url(r'^/grafik/(?P<bulan>\d+)/(?P<tahun>\d+)$', views.tampil_grafik, name="tampil_grafik"),
	url(r'^/cetak/(?P<bulan>\d+)/(?P<tahun>\d+)$', views.cetak_daftar_hadir, name="cetak"),
]
