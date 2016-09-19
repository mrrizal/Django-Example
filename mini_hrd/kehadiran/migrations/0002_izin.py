# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
        ('kehadiran', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izin',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('jenis_kehadiran', models.CharField(choices=[('izin', 'Izin'), ('cuti', 'Cuti')], max_length=20)),
                ('waktu_mulai', models.DateField()),
                ('waktu_selesai', models.DateField()),
                ('alasan', models.TextField()),
                ('disetujui', models.BooleanField(default=False)),
                ('karyawan', models.ForeignKey(to='karyawan.Karyawan')),
            ],
        ),
    ]
