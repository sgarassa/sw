from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models

# Create your models here.

class Azienda(models.Model):
	AZ01_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Utente')
	#AZ01_codiceazienda = models.IntegerField(primary_key=True, verbose_name='Azienda')
	AZ01_ragionesoc = models.CharField(max_length=60,verbose_name='Ragione Sociale')
	AZ01_indirizzo = models.CharField(max_length=50, verbose_name='Indirizzo')
	AZ01_citta = models.CharField(max_length=50, verbose_name='Citta')
	AZ01_provincia = models.CharField(max_length=2, verbose_name='Provincia')
	AZ01_cap = models.CharField(max_length=5,verbose_name='CAP')
	AZ01_piva = models.CharField(max_length=12,verbose_name='Partita Iva')
	AZ01_codfiscp = models.CharField(max_length=12,verbose_name='Codice Fiscale')
	AZ01_ammin = models.CharField(max_length=40,verbose_name='Amministratore')
	AZ01_medcomp = models.CharField(max_length=40,verbose_name='Medico Competente')
	AZ01_rls = models.CharField(max_length=40,verbose_name='RLS')
	AZ01_rspp = models.CharField(max_length=40,verbose_name='RSPP')
	AZ01_ciclprod = models.CharField(max_length=40,verbose_name='Ciclo Produttivo')
	def __unicode__(self):
		return str(self.AZ01_ragionesoc)
	class Meta:
		verbose_name_plural = 'Aziende'

class MisPrevInc(models.Model):
	#MS01_codice = models.IntegerField(primary_key=True,verbose_name='Codice')
	MS01_descrizione = models.CharField(max_length=50,verbose_name='Descrizione')
	def __unicode__(self):
		return str(self.MS01_descrizione)
	class Meta:
		verbose_name_plural = 'Misure preventive incendi'

class MisPrevVibra(models.Model):
	#MS02_codice = models.IntegerField(primary_key=True,verbose_name='Codice')
	MS02_descrizione = models.CharField(max_length=50,verbose_name='Descrizione')
	def __unicode__(self):
		return str(self.MS02_descrizione)
	class Meta:
		verbose_name_plural = 'Misure preventive vibrazioni'




class Reparti(models.Model):
	SCARSA = 'SC'
	FAVORITA = 'FV'
	ELEVATA = 'EL'
	PROB_INCENDIO = (
        (SCARSA, 'SCARSA'),
        (FAVORITA, 'FAVORITA'),
        (ELEVATA, 'ELEVATA'),
        )
	BASSA = 'BS'
	LIMITATA = 'LM'
	NOTEVOLE = 'NT'
	PROB_PROPAGAZIONE = (
        (BASSA, 'BASSA'),
        (LIMITATA, 'LIMITATA'),
        (NOTEVOLE, 'NOTEVOLE'),
        )
	RP01_codiceazienda = models.ForeignKey(Azienda, verbose_name='Azienda')
	#RP01_codicerep = models.IntegerField(primary_key=True,verbose_name='Codice Reparto')
	RP01_descrizione = models.CharField(max_length=50,verbose_name='Descrizione')
	RP01_codicemisprevinc = models.ManyToManyField(MisPrevInc, verbose_name='Misure Preventive Incendi')
	RP01_probinc = models.CharField(
		max_length=2, 
		choices = PROB_INCENDIO, 
		default = SCARSA,
	verbose_name='Probabilita incendio')
	RP01_probprobagaz = models.CharField(
		max_length=2, 
		choices = PROB_PROPAGAZIONE, 
		default = BASSA,
	verbose_name='Probabilita di propagazione')
	def __unicode__(self):
		return str(self.RP01_descrizione)
	class Meta:
		verbose_name_plural = 'Reparti'


class Mansione(models.Model):
	#MS03_codmansione = models.IntegerField(primary_key=True,verbose_name='Codice')
	MS04_descrizione = models.CharField(max_length=50,verbose_name='Descrizione')
	def __unicode__(self):
		return str(self.MS04_descrizione)
	class Meta:
		verbose_name_plural = 'Mansione'




class Locali(models.Model):
	LC01_codiceazienda = models.ForeignKey(Azienda, verbose_name='Azienda')
	#LC01_codiceloc = models.IntegerField(primary_key=True,verbose_name='Codice Locale')
	LC01_descrizione = models.CharField(max_length=50,verbose_name='Descrizione')
	LC01_dimensioni = models.CharField(max_length=20, null=True, verbose_name='Dimensioni')
	def __unicode__(self):
		return str(self.LC01_descrizione)
	class Meta:
		verbose_name_plural = 'Locali'


class Dipendenti(models.Model):
	DP01_codiceazienda = models.ForeignKey(Azienda, verbose_name='Azienda')
	DP01_codicemansione = models.ForeignKey(Mansione, verbose_name='Mansione')
	#DP01_codicedip = models.IntegerField(primary_key=True,verbose_name='Codice Dipendente')
	DP01_descrizione = models.CharField(max_length=50,verbose_name='Descrizione')
	DP01_datanascita = models.DateField(null=True, verbose_name='Data di nascita')
	def __unicode__(self):
		return str(self.DP01_descrizione)
	class Meta:
		verbose_name_plural = 'Dipendenti'
