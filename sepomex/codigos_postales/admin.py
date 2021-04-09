from django.contrib import admin
from codigos_postales.models.estado import Estado
from codigos_postales.models.municipio import Municipio
from codigos_postales.models.asentamiento import Asentamiento
from codigos_postales.models.codigo_postal import CodigoPostal

# class EstadoAdmin(admin.ModelAdmin):
#     list_display = ('estado', 'fecha_ultima_actualizacion')
#     list_filter = ('fecha_ultima_actualizacion')




admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Asentamiento)
admin.site.register(CodigoPostal)