# imports para manejar las rutas
from django.urls import path

# imports de vistas
from codigos_postales.views.estado_list import EstadoList
from codigos_postales.views.municipio_list import MunicipioList

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

]
