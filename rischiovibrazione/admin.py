from django.contrib import admin
from tabgenerali.models import *
from rischiovibrazione.models import *
from django import forms



# Register your models here.
class StrumentiOption(admin.ModelAdmin):
	list_display = ('ST01_codiceazienda',  'ST01_descrizione', 'ST01_tipovibr')
	search_fields = ('ST01_descrizione',)
	raw_id_fields = ('ST01_codiceazienda',)
	def azie(self, Strumenti):
		return Strumenti.ST01_codiceazienda.AZ01_ragionesoc

class DipendentiStrumentiOption(admin.ModelAdmin):
	list_display = ('DS01_codiceazienda', 'DS01_codicestr', 'DS01_tempoutilizzo')



admin.site.register(Strumenti, StrumentiOption)
admin.site.register(DipendentiStrumenti, DipendentiStrumentiOption)



