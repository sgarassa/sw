# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabgenerali', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparti',
            name='RP01_codicemisprevinc',
            field=models.ManyToManyField(to='tabgenerali.MisPrevInc', verbose_name='Misure Preventive Incendi'),
        ),
    ]
