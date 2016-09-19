# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kehadiran',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('jenis_kehadiran', models.CharField(choices=[('izin', 'Izin'), ('cuti', 'Cuti'), ('alpa', 'Tanpa Alasan'), ('hadir', 'Hadir')], max_length=20)),
                ('waktu', models.DateField()),
                ('karyawan', models.ForeignKey(to='karyawan.Karyawan')),
            ],
        ),
    ]
