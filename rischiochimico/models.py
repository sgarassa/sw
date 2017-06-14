from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models
import tabgenerali


# Create your models here.

class Sostanze(models.Model):
	NOSCELTA = 'NS'
	METSTIM = 'MS'
	CUTOFF = 'CO'
	ALGORITMO_CHOICES = (
        (NOSCELTA, '-------'),
        (METSTIM, 'Metodo Stimato'),
        (CUTOFF, 'CUT OFF'),
        )
	SS01_codiceazienda = models.ForeignKey(tabgenerali.models.Azienda, verbose_name='Azienda')
	SS01_codicesost = models.CharField(max_length=20,verbose_name='Codice Sostanza')
	SS01_descrizione = models.CharField(max_length=50,verbose_name='Descrizione')
	SS01_tiposostanza = models.CharField(max_length=50,verbose_name='Tipo Sostanza')
	SS01_dispersione = models.CharField(max_length=50,verbose_name='Dispersione')
	SS01_codicedip = models.ManyToManyField(tabgenerali.models.Dipendenti, verbose_name='Dipendente')
	SS01_disponibilita = models.CharField(max_length=50,verbose_name='Disponibilita')
	SS01_quantita = models.DecimalField(max_digits=6, decimal_places=4,verbose_name='Quantita')
	SS01_tipoalgoritmo = models.CharField(
		max_length=2, 
		choices = ALGORITMO_CHOICES, 
		default = NOSCELTA,
	verbose_name='Metodo di calcolo')
	def __unicode__(self):
		return str(self.SS01_codicesost)
	class Meta:
		verbose_name_plural = 'Sostanze'

