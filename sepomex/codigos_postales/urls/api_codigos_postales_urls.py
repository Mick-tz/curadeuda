# imports para manejar las rutas
from django.urls import path

# imports de vistas
from codigos_postales.views.estado_list import EstadoList
from codigos_postales.views.municipio_list import MunicipioList
from codigos_postales.views.asentamiento_list import AsentamientoList
from codigos_postales.views.codigo_postal_list import CodigoPostalList

urlpatterns = [

    path(
        'estados',
        view=EstadoList.as_view(),
        name='estados_list_view',
    ),

    path(
        'municipios',
        view=MunicipioList.as_view(),
        name='municipios_list_view',
    ),

    path(
        'asentamientos',
        view=AsentamientoList.as_view(),
        name='asentamientos_list_view',
    ),

    path(
        'codigos_postales',
        view=CodigoPostalList.as_view(),
        name='codigos_postales_list_view',
    ),

]
