from django.db import models
from karyawan.models import Karyawan

class Kehadiran(models.Model):
	JENIS_KEHADIRAN_CHOICES = (('izin', 'Izin'), ('cuti', 'Cuti'), ('alpa', 'Tanpa Alasan'), ('hadir', 'Hadir'))
	karyawan = models.ForeignKey(Karyawan)
	jenis_kehadiran = models.CharField(max_length=20, choices=JENIS_KEHADIRAN_CHOICES)
	waktu = models.DateField()

	def __str__(self):
		return self.karyawan.nama

class Izin(models.Model):
	JENIS_KEHADIRAN_CHOICES = (('izin', 'Izin'), ('cuti', 'Cuti'))
	karyawan = models.ForeignKey(Karyawan)
	jenis_kehadiran = models.CharField(max_length=20, choices=JENIS_KEHADIRAN_CHOICES)
	waktu_mulai = models.DateField()
	waktu_berhenti = models.DateField()
	alasan = models.TextField()
	disetujui = models.BooleanField(default=False)

	def __str__(self):
		return self.karyawan.nama	