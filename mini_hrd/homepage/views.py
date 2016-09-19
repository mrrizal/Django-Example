from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView, RedirectView
from django.contrib.auth import authenticate, logout, login
from homepage.forms import UserForm
from karyawan.models import Akun
from django.contrib import messages

class LoginView(FormView):
	success_url =  'hrd:index'
	template_name = 'homepage/login.html'
	form_class = UserForm

	def get(self, request):
		if(not request.user.is_authenticated()):
			form = self.form_class(None)
			return render(request, self.template_name, {'form':form})
		return redirect(self.success_url)
	
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			if user is not None:
				if user.is_active:
					try:
						akun = Akun.objects.get(akun=user.id)
						login(request, user)

						# simpan ke session
						request.session['karyawan_id'] = akun.karyawan.id
						request.session['jenis_akun'] = akun.jenis_akun
						request.session['username'] = request.POST['username']

						return redirect(self.success_url)
					except:
						messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administrator')
				else:
					messages.add_message(request, messages.INFO, 'User belum terverivikasi')
			else:
				messages.add_message(request, messages.INFO, 'Username atau password salah')				

		return render(request, self.template_name, {'form':form})

def logout_view(request):
	logout(request)
	return redirect('hrd:index')


def index(request):
	return redirect('profile:profile')