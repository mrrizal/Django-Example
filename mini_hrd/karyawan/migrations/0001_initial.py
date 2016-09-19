# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('jenis_akun', models.CharField(choices=[('karyawan', 'Karyawan'), ('admin', 'Administrator')], max_length=10)),
                ('akun', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nama', models.CharField(max_length=100)),
                ('keterangan', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nama', models.CharField(max_length=100)),
                ('keterangan', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField(blank=True)),
                ('jenis_kelamin', models.CharField(choices=[('pria', 'Pria'), ('wanita', 'Wanita')], max_length=10)),
                ('jenis_karyawan', models.CharField(choices=[('magang', 'Magang'), ('kontrak', 'Kontrak'), ('tetap', 'Tetap')], max_length=10)),
                ('no_telepon', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('no_rekening', models.CharField(max_length=100)),
                ('pemilik_rekening', models.CharField(max_length=100)),
                ('divisi', models.ForeignKey(to='karyawan.Divisi')),
                ('jabatan', models.ForeignKey(to='karyawan.Jabatan')),
            ],
        ),
        migrations.AddField(
            model_name='akun',
            name='karyawan',
            field=models.ForeignKey(to='karyawan.Karyawan'),
        ),
    ]
