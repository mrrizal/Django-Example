from django import forms
from .models import Album
from django.contrib.auth.models import User

#form untuk album
class AlbumForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AlbumForm, self).__init__(*args, **kwargs)
		self.fields['artist'].widget.attrs = {'class':'form-control'}
		self.fields['album_title'].widget.attrs = {'class':'form-control'}
		self.fields['genre'].widget.attrs = {'class':'form-control'}

	class Meta:
		model = Album
		fields = '__all__'

#form untuk user
class UserForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs={'class':'form-control'}
		self.fields['email'].widget.attrs={'class':'form-control'}
	
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password']