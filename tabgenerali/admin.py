from django.contrib import admin
from tabgenerali.models import *
from django import forms


# Register your models here.
class AziendeOption(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super(AziendeOption, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(AZ01_user_id=request.user)
	list_display = ( 'AZ01_ragionesoc', 'AZ01_indirizzo','AZ01_citta')
	search_fields = ('AZ01_ragionesoc',)
	#limit_chois_to = request.user.is_authenticated



class RepartiOption(admin.ModelAdmin):
	list_display = ('RP01_codiceazienda', 'RP01_descrizione')
	search_fields = ('RP01_descrizione',)
	raw_id_fields = ('RP01_codiceazienda',)
	def azie(self, Reparti):
		return Reparti.RP01_codiceazienda.AZ01_ragionesoc


class MisPrevIncOption(admin.ModelAdmin):
	list_display = ('MS01_descrizione',)


class MisPrevVibraOption(admin.ModelAdmin):
	list_display = ('MS02_descrizione',)


class LocaliOption(admin.ModelAdmin):
	list_display = ('LC01_codiceazienda', 'LC01_descrizione', 'LC01_dimensioni')
	search_fields = ('LC01_descrizione',)
	raw_id_fields = ('LC01_codiceazienda',)
	def azie(self, Locali):
		return Locali.LC01_codiceazienda.AZ01_ragionesoc


class DipendentiOption(admin.ModelAdmin):
	list_display = ('DP01_codiceazienda', 'DP01_descrizione')
	search_fields = ( 'DP01_descrizione',)
	raw_id_fields = ('DP01_codiceazienda', 'DP01_codicemansione',)
	def azie(self, Dipendenti):
		return Dipendenti.DP01_codiceazienda.AZ01_ragionesoc


class MansioneOption(admin.ModelAdmin):
	list_display = ('MS04_descrizione',)
	search_fields = ('MS04_descrizione',)


admin.site.register(Azienda, AziendeOption)
admin.site.register(Reparti, RepartiOption)
admin.site.register(MisPrevInc, MisPrevIncOption)
admin.site.register(MisPrevVibra, MisPrevVibraOption)
admin.site.register(Locali, LocaliOption)
admin.site.register(Dipendenti, DipendentiOption)
admin.site.register(Mansione, MansioneOption)


