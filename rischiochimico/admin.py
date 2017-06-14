from django.contrib import admin
from tabgenerali.models import *
from rischiochimico.models import *
from django import forms


# Register your models here.
class SostanzeOption(admin.ModelAdmin):
	list_display = ('SS01_codiceazienda', 'SS01_codicesost', 'SS01_descrizione', 'SS01_tiposostanza', 'SS01_dispersione', 'SS01_disponibilita', 'SS01_quantita', 'SS01_tipoalgoritmo')
	search_fields = ('SS01_codicesost', 'SS01_descrizione',)
	raw_id_fields = ('SS01_codiceazienda',)
	def azie(self, Sostanze):
		return Sostanze.SS01_codiceazienda.AZ01_ragionesoc


admin.site.register(Sostanze, SostanzeOption)

