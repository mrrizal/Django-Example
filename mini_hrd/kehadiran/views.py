from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import FormView, RedirectView
from kehadiran.forms import Filter_kehadiran, IzinForm
from kehadiran.models import Kehadiran, Izin
from django.contrib.auth.decorators import login_required
from karyawan.models import Karyawan
from django.http import HttpResponse
from django.contrib import messages
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors

class KehadiranView(FormView):
	success_url = 'kehadiran:index'
	template_name = 'kehadiran/index.html'
	form_class = Filter_kehadiran

	def get(self, request):
		form = self.form_class(None)
		try:
			daftar_hadir = Kehadiran.objects.filter(karyawan_id=request.session['karyawan_id'], waktu__year=request.session['tahun'], waktu__month=request.session['bulan'])
		except:
			daftar_hadir = None			
		return render(request, self.template_name, {'form':form, 'daftar_hadir':daftar_hadir})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			request.session['tahun'] = request.POST['tahun']
			request.session['bulan'] = request.POST['bulan']
			daftar_hadir = Kehadiran.objects.filter(karyawan_id=request.session['karyawan_id'], waktu__year=request.POST['tahun'], waktu__month=request.POST['bulan'])
			return render(request, self.template_name, {'form':form, 'daftar_hadir':daftar_hadir})

		try:
			del request.session['tahun']
			del request.session['bulan']
		except:
			pass
			
		return render(request, self.template_name, {'form':form})		



@login_required(login_url=settings.LOGIN_URL)
def pengajuan_izin(request):
	template_name = 'kehadiran/tambah-izin.html'

	if request.method=='POST':
		form_data = request.POST
		form = IzinForm(form_data)

		if form.is_valid():
			izin = Izin(
					karyawan = Karyawan.objects.get(id=request.session['karyawan_id']),
					jenis_kehadiran = request.POST['jenis_kehadiran'],
					# jika menggunakan datetimefield gunakan script dibawah ini
					# waktu_mulai = str(request.POST['waktu_mulai_year'])+"-"+str(request.POST['waktu_mulai_month'])+"-"+str(request.POST['waktu_mulai_day']),
					# waktu_berhenti = str(request.POST['waktu_berhenti_year'])+"-"+str(request.POST['waktu_berhenti_month'])+"-"+str(request.POST['waktu_berhenti_day']),
					waktu_mulai = request.POST['waktu_mulai'],
					waktu_berhenti = request.POST['waktu_berhenti'],
					alasan =  request.POST['alasan'],
				)
			izin.save()
			form = IzinForm(None)
			messages.add_message(request, messages.INFO, 'Berhasil manambahkan penganjuan izin')
			return render(request, template_name, {'form':form})
	else:
		form = IzinForm(None)
	return render(request, template_name, {'form':form})

@login_required(login_url=settings.LOGIN_URL)
def daftar_izin(request):
	template_name = 'kehadiran/daftar-izin.html'
	daftar_izin = Izin.objects.filter(karyawan_id=request.session['karyawan_id']).order_by('-waktu_mulai')

	# for pagination
	paginator = Paginator(daftar_izin, 5)
	page = request.GET.get('page')
	try:
		daftar_izin = paginator.page(page)
	except PageNotAnInteger:
		daftar_izin = paginator.page(1)
	except EmptyPage:
		daftar_izin = paginator.page(paginator.num_pages)

	return render(request, template_name, {'daftar_izin':daftar_izin})

@login_required(login_url=settings.LOGIN_URL)
def tampil_grafik(request, bulan, tahun):
    temp_chart_data = []
    daftar_hadir = Kehadiran.objects.filter(waktu__year=tahun, waktu__month=bulan, karyawan__id=request.session['karyawan_id'])

    temp_chart_data.append({ "x":"hadir", "a":daftar_hadir.filter(jenis_kehadiran='hadir').count() })
    temp_chart_data.append({ "x":"izin", "a":daftar_hadir.filter(jenis_kehadiran='izin').count() })
    temp_chart_data.append({ "x":"alpa", "a":daftar_hadir.filter(jenis_kehadiran='alpa').count() })
    temp_chart_data.append({ "x":"cuti", "a":daftar_hadir.filter(jenis_kehadiran='cuti').count() })

    chart_data = json.dumps({"data":temp_chart_data})               

    return render(request, 'kehadiran/tampil-grafik.html', {'chart_data':chart_data, 'bulan':bulan, 'tahun':tahun})

@login_required(login_url=settings.LOGIN_URL)
def cetak_daftar_hadir(request, bulan, tahun):
	# pengaturan respon berformat pdf
	filename = "dafar_hadir_" + str(bulan) + str(tahun)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="' + filename + '.pdf"'

	# mengambil data kehadiran dan mengubahnya menjadi data untuk table
	data = Kehadiran.objects.filter(waktu__year=tahun, waktu__month=bulan, karyawan__id=request.session['karyawan_id'])
	table_data = []
	table_data.append(['Tanggal', 'Status'])
	for x in data:
		table_data.append([x.waktu, x.jenis_kehadiran])

	# membuat dokumen baru
	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
	styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
	table_style = TableStyle([
	                           ('ALIGN',(1,1),(-2,-2),'RIGHT'),
	                           ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
	                           ('VALIGN',(0,0),(0,-1),'TOP'),
	                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
	                       ])
	kehadiran_table = Table(table_data, colWidths=[doc.width/4.0]*2)
	kehadiran_table.setStyle(table_style)

	# mengisi pdf
	content = []
	content.append(Paragraph('Daftar Kehadiran %s/%s' % (bulan, tahun), styles['Title']))
	content.append(Spacer(1,12))
	content.append(Paragraph('Berikut ini adalah hasil rekam jejak kehadiran Anda selama bulan %s tahun %s:' % (bulan, tahun), styles['Normal']))
	content.append(Spacer(1,12))
	content.append(kehadiran_table)
	content.append(Spacer(1,36))
	content.append(Paragraph('Mengetahui, ', styles['Normal']))
	content.append(Spacer(1,48))
	content.append(Paragraph('Mira Kumalasari, Head of Department PT. Ngabuburit Sentosa Sejahtera. ', styles['Normal']))

	# menghasilkan pdf untk di download
	doc.build(content)
	return response
