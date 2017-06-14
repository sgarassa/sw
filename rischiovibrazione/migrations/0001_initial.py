# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabgenerali', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DipendentiStrumenti',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('DS01_tempoutilizzo', models.CharField(max_length=20, verbose_name='Tempo di utilizzo')),
                ('DS01_codiceazienda', models.ForeignKey(verbose_name='Azienda', to='tabgenerali.Azienda')),
                ('DS01_codicedip', models.ManyToManyField(verbose_name='Dipendente', to='tabgenerali.Dipendenti')),
            ],
            options={
                'verbose_name_plural': 'Strumentazione dei dipendenti',
            },
        ),
        migrations.CreateModel(
            name='Strumenti',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ST01_descrizione', models.CharField(max_length=50, verbose_name='Descrizione')),
                ('ST01_tipovibr', models.CharField(max_length=2, verbose_name='Tipologia Vibrazione', default='CI', choices=[('CI', 'CORPO INTERO'), ('MB', 'MANO BRACCIO')])),
                ('ST01_produttore', models.CharField(max_length=50, verbose_name='Produttore', null=True)),
                ('ST01_modello', models.CharField(max_length=50, verbose_name='Modello', null=True)),
                ('ST01_vibrazcostr', models.DecimalField(verbose_name='Vibraz. Costruttore', null=True, decimal_places=4, max_digits=6)),
                ('ST01_accvibrazx', models.DecimalField(verbose_name='Accelerazione X', null=True, decimal_places=4, max_digits=6)),
                ('ST01_accvibrazy', models.DecimalField(verbose_name='Accelerazione Y', null=True, decimal_places=4, max_digits=6)),
                ('ST01_accvibrazz', models.DecimalField(verbose_name='Accelerazione Z', null=True, decimal_places=4, max_digits=6)),
                ('ST01_accvibrazw', models.DecimalField(verbose_name='Accelerazione W', null=True, decimal_places=4, max_digits=6)),
                ('ST01_origmis', models.CharField(max_length=2, verbose_name='Origine Misurazione', default='MS', choices=[('LC', 'LIBRETTO DEL COSTRUTTORE'), ('MS', 'MISURAZIONE'), ('BD', 'BANCA DATI')])),
                ('ST01_note', models.CharField(max_length=100, verbose_name='Note', null=True)),
                ('ST01_tempoesp', models.DecimalField(verbose_name='Tempo di esposizione', null=True, decimal_places=4, max_digits=6)),
                ('ST01_fattcorr', models.DecimalField(verbose_name='Fattore di correzione', null=True, decimal_places=4, max_digits=6)),
                ('ST01_codiceazienda', models.ForeignKey(verbose_name='Azienda', to='tabgenerali.Azienda')),
                ('ST01_codiceloc', models.ManyToManyField(verbose_name='Locale', to='tabgenerali.Locali')),
                ('ST01_codicemisprevvibra', models.ManyToManyField(verbose_name='Misure preventive vibrazioni', to='tabgenerali.MisPrevVibra')),
            ],
            options={
                'verbose_name_plural': 'Strumenti',
            },
        ),
        migrations.AddField(
            model_name='dipendentistrumenti',
            name='DS01_codicestr',
            field=models.ForeignKey(verbose_name='Strumento', to='rischiovibrazione.Strumenti'),
        ),
    ]
