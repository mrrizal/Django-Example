from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('homepage.urls', namespace='hrd')),
	url(r'^HRD/', include('homepage.urls', namespace='hrd')),
	url(r'^HRD/karyawan',include('karyawan.urls', namespace='profile')),
	url(r'^HRD/kehadiran',include('kehadiran.urls', namespace='kehadiran'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
