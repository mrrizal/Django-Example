# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0002_izin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='izin',
            old_name='waktu_selesai',
            new_name='waktu_berhenti',
        ),
    ]
