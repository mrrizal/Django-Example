from django import forms
from kehadiran.models import Izin
from django.forms.extras.widgets import SelectDateWidget

tahun_choices = (
		('2016','2016'),
		('2015','2015'),
		('2014','2014'),
	)
bulan_choices = (
		('01','Januari'),
		('02','Februari'),
		('03','Maret'),
		('04','April'),
		('05','Mei'),
		('06','Juni'),
		('07','Juli'),
		('08','Agustus'),
		('09','September'),
		('10','Oktober'),
		('11','November'),
		('12','Desember'),
	)

class Filter_kehadiran(forms.Form):
	tahun = forms.ChoiceField(choices=tahun_choices)
	bulan = forms.ChoiceField(choices=bulan_choices)

class IzinForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(IzinForm, self).__init__(*args, **kwargs)
		self.fields['jenis_kehadiran'].widget.attrs={'class':'form-control'}
		self.fields['waktu_mulai'].widget.attrs={'class':'form-control'}
		self.fields['waktu_berhenti'].widget.attrs={'class':'form-control'}

	class Meta:
		model = Izin
		fields = ['jenis_kehadiran', 'waktu_mulai', 'waktu_berhenti', 'alasan']
		labels = {'jenis_kehadiran' : 'Jenis Izin','waktu_mulai' : 'Mulai Izin','waktu_berhenti' : 'Berhenti Izin','alasan' : 'Alasan Izin'}
		widgets = {
			'alasan' : forms.Textarea(attrs={'class':'form-control', 'cols':50, 'rows':10}),
			#'waktu_mulai' : SelectDateWidget,
			#'waktu_berhenti' : SelectDateWidget,
		}