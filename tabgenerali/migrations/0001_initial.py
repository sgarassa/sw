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
            name='Azienda',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('AZ01_ragionesoc', models.CharField(verbose_name='Ragione Sociale', max_length=60)),
                ('AZ01_indirizzo', models.CharField(verbose_name='Indirizzo', max_length=50)),
                ('AZ01_citta', models.CharField(verbose_name='Citta', max_length=50)),
                ('AZ01_provincia', models.CharField(verbose_name='Provincia', max_length=2)),
                ('AZ01_cap', models.CharField(verbose_name='CAP', max_length=5)),
                ('AZ01_piva', models.CharField(verbose_name='Partita Iva', max_length=12)),
                ('AZ01_codfiscp', models.CharField(verbose_name='Codice Fiscale', max_length=12)),
                ('AZ01_ammin', models.CharField(verbose_name='Amministratore', max_length=40)),
                ('AZ01_medcomp', models.CharField(verbose_name='Medico Competente', max_length=40)),
                ('AZ01_rls', models.CharField(verbose_name='RLS', max_length=40)),
                ('AZ01_rspp', models.CharField(verbose_name='RSPP', max_length=40)),
                ('AZ01_ciclprod', models.CharField(verbose_name='Ciclo Produttivo', max_length=40)),
                ('AZ01_user', models.ForeignKey(verbose_name='Utente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Aziende',
            },
        ),
        migrations.CreateModel(
            name='Dipendenti',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('DP01_descrizione', models.CharField(verbose_name='Descrizione', max_length=50)),
                ('DP01_datanascita', models.DateField(verbose_name='Data di nascita', null=True)),
                ('DP01_codiceazienda', models.ForeignKey(verbose_name='Azienda', to='tabgenerali.Azienda')),
            ],
            options={
                'verbose_name_plural': 'Dipendenti',
            },
        ),
        migrations.CreateModel(
            name='Locali',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('LC01_descrizione', models.CharField(verbose_name='Descrizione', max_length=50)),
                ('LC01_dimensioni', models.CharField(verbose_name='Dimensioni', null=True, max_length=20)),
                ('LC01_codiceazienda', models.ForeignKey(verbose_name='Azienda', to='tabgenerali.Azienda')),
            ],
            options={
                'verbose_name_plural': 'Locali',
            },
        ),
        migrations.CreateModel(
            name='Mansione',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('MS04_descrizione', models.CharField(verbose_name='Descrizione', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Mansione',
            },
        ),
        migrations.CreateModel(
            name='MisPrevInc',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('MS01_descrizione', models.CharField(verbose_name='Descrizione', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Misure preventive incendi',
            },
        ),
        migrations.CreateModel(
            name='MisPrevVibra',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('MS02_descrizione', models.CharField(verbose_name='Descrizione', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Misure preventive vibrazioni',
            },
        ),
        migrations.CreateModel(
            name='Reparti',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('RP01_descrizione', models.CharField(verbose_name='Descrizione', max_length=50)),
                ('RP01_probinc', models.CharField(default='SC', choices=[('SC', 'SCARSA'), ('FV', 'FAVORITA'), ('EL', 'ELEVATA')], verbose_name='Probabilita incendio', max_length=2)),
                ('RP01_probprobagaz', models.CharField(default='BS', choices=[('BS', 'BASSA'), ('LM', 'LIMITATA'), ('NT', 'NOTEVOLE')], verbose_name='Probabilita di propagazione', max_length=2)),
                ('RP01_codiceazienda', models.ForeignKey(verbose_name='Azienda', to='tabgenerali.Azienda')),
                ('RP01_codicemisprevinc', models.ManyToManyField(verbose_name='Misure Preventive Incendi', null=True, to='tabgenerali.MisPrevInc')),
            ],
            options={
                'verbose_name_plural': 'Reparti',
            },
        ),
        migrations.AddField(
            model_name='dipendenti',
            name='DP01_codicemansione',
            field=models.ForeignKey(verbose_name='Mansione', to='tabgenerali.Mansione'),
        ),
    ]
