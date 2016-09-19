from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from karyawan.models import Karyawan
from django.http import HttpResponse


@login_required(login_url=settings.LOGIN_URL)
def profile(request):
	karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
	return render(request, 'karyawan/profile.html', {'karyawan':karyawan})

@login_required(login_url=settings.LOGIN_URL)
def ganti_foto(request):
    karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
    karyawan.foto = request.FILES['files']
    karyawan.save()

    return redirect('/')