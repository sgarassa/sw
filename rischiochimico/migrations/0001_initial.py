# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabgenerali', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sostanze',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('SS01_codicesost', models.CharField(verbose_name='Codice Sostanza', max_length=20)),
                ('SS01_descrizione', models.CharField(verbose_name='Descrizione', max_length=50)),
                ('SS01_tiposostanza', models.CharField(verbose_name='Tipo Sostanza', max_length=50)),
                ('SS01_dispersione', models.CharField(verbose_name='Dispersione', max_length=50)),
                ('SS01_disponibilita', models.CharField(verbose_name='Disponibilita', max_length=50)),
                ('SS01_quantita', models.DecimalField(decimal_places=4, verbose_name='Quantita', max_digits=6)),
                ('SS01_tipoalgoritmo', models.CharField(default='NS', verbose_name='Metodo di calcolo', max_length=2, choices=[('NS', '-------'), ('MS', 'Metodo Stimato'), ('CO', 'CUT OFF')])),
                ('SS01_codiceazienda', models.ForeignKey(verbose_name='Azienda', to='tabgenerali.Azienda')),
                ('SS01_codicedip', models.ManyToManyField(verbose_name='Dipendente', to='tabgenerali.Dipendenti')),
            ],
            options={
                'verbose_name_plural': 'Sostanze',
            },
        ),
    ]
