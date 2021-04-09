from django.contrib import admin
from codigos_postales.models.estado import Estado
from codigos_postales.models.municipio import Municipio
from codigos_postales.models.asentamiento import Asentamiento
from codigos_postales.models.codigo_postal import CodigoPostal

class CodigoPostalAdmin(admin.ModelAdmin):
    list_display = ('d_codigo', 'id_asenta_cpcons')
    search_fields = ('d_codigo',)

class AsentamientoAdmin(admin.ModelAdmin):
    list_display = ('id_asenta_cpcons', 'd_asenta', 'd_tipo_asenta', 'c_tipo_asenta', 'c_mnpio')
    list_filter = ('d_tipo_asenta',)
    search_fields = ('id_asenta_cpcons',)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('c_estado', 'd_estado')
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('c_mnpio', 'd_mnpio', 'c_estado')
    list_filter = ('c_estado',)
    search_fields = ('c_mnpio',)


admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Asentamiento, AsentamientoAdmin)
admin.site.register(CodigoPostal, CodigoPostalAdmin)