from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models
import tabgenerali

# Create your models here.

class Strumenti(models.Model):
	CORINT = 'CI'
	MANBA = 'MB'
	TIPO_VIBRAZIONE = (
        (CORINT, 'CORPO INTERO'),
        (MANBA, 'MANO BRACCIO'),
        )
	LIBCOR = 'LC'
	MISURA = 'MS'
	BNCDAT = 'BD'
	PROV_VIBRAZIONE = (
        (LIBCOR, 'LIBRETTO DEL COSTRUTTORE'),
        (MISURA, 'MISURAZIONE'),
	(BNCDAT, 'BANCA DATI'),
        )
	ST01_codiceazienda = models.ForeignKey(tabgenerali.models.Azienda,verbose_name='Azienda')
	#ST01_codicestrum = models.IntegerField(primary_key=True,verbose_name='Codice Strumento')
	ST01_descrizione = models.CharField(max_length=50,verbose_name='Descrizione')
	ST01_tipovibr = models.CharField(
		max_length=2, 
		choices = TIPO_VIBRAZIONE, 
		default = CORINT,
	verbose_name='Tipologia Vibrazione')
	ST01_produttore = models.CharField(max_length=50, null=True, verbose_name='Produttore')
	ST01_modello = models.CharField(max_length=50, null=True, verbose_name='Modello')
	ST01_vibrazcostr = models.DecimalField(max_digits=6, decimal_places=4, null=True, verbose_name='Vibraz. Costruttore')
	ST01_accvibrazx = models.DecimalField(max_digits=6, decimal_places=4, null=True, verbose_name='Accelerazione X')
	ST01_accvibrazy = models.DecimalField(max_digits=6, decimal_places=4, null=True, verbose_name='Accelerazione Y')
	ST01_accvibrazz = models.DecimalField(max_digits=6, decimal_places=4, null=True, verbose_name='Accelerazione Z')
	ST01_accvibrazw = models.DecimalField(max_digits=6, decimal_places=4, null=True, verbose_name='Accelerazione W')
	ST01_origmis = models.CharField(
		max_length=2, 
		choices = PROV_VIBRAZIONE, 
		default = MISURA,
		verbose_name='Origine Misurazione')
	ST01_note = models.CharField(max_length=100, null=True, verbose_name='Note')
	ST01_codicemisprevvibra = models.ManyToManyField(tabgenerali.models.MisPrevVibra, verbose_name='Misure preventive vibrazioni')
	ST01_codiceloc = models.ManyToManyField(tabgenerali.models.Locali ,verbose_name='Locale')
	ST01_tempoesp = models.DecimalField(max_digits=6, decimal_places=4, null=True, verbose_name='Tempo di esposizione')
	ST01_fattcorr = models.DecimalField(max_digits=6, decimal_places=4, null=True, verbose_name='Fattore di correzione')
	def __unicode__(self):
		return str(self.ST01_descrizione)
	class Meta:
		verbose_name_plural = 'Strumenti'



class DipendentiStrumenti(models.Model):
	DS01_codiceazienda = models.ForeignKey(tabgenerali.models.Azienda, verbose_name='Azienda')
	DS01_codicestr = models.ForeignKey(Strumenti, verbose_name='Strumento')
	DS01_codicedip = models.ManyToManyField(tabgenerali.models.Dipendenti, verbose_name='Dipendente')
	DS01_tempoutilizzo = models.CharField(max_length=20,verbose_name='Tempo di utilizzo')
	class Meta:
		verbose_name_plural = 'Strumentazione dei dipendenti'

