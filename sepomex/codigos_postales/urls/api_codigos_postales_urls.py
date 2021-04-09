# imports para manejar las rutas
from django.urls import path

# imports de vistas
from codigos_postales.views.estado_list import EstadoList

urlpatterns = [

    path(
        'estados',
        view=EstadoList.as_view(),
        name='estados_view',
    ),

]
