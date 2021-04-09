# utils
from django.core.paginator import Paginator
from sepomex.serializers.paginator_serializer import PaginatorSerializer

# modelos y serializadores de asentamientos
from codigos_postales.models.asentamiento import Asentamiento
from codigos_postales.serializers.serializador_asentamiento import SerializadorAsentamiento

# manejo de autenticacion y respuesta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AsentamientoList(APIView):
    """
    View para listar los asentamientos
    """
    # descomentar la siguiente línea cuando se tenga implementado el sistema de usuarios 
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # obtenemos la informacion de la paginación, en caso de no ser provista, el default de page_size será 20.
        page_number = int(request.GET['page_number']) if 'page_number' in request.GET else 1
        page_size = int(request.GET['page_size']) if 'page_size' in request.GET else 20
        
        # el queryset consta de todos los asentamientos
        asentamientos = Asentamiento.objects.all()

        # creamos paginator con la cantidad de asentamientos requerida
        paginator = Paginator(
            object_list=asentamientos,
            per_page=page_size, 
        )

        # usando el paginator, serializamos los asentamientos requeridos junto a la informacion de paginacion
        serializer = SerializadorAsentamiento(
            paginator.page(number=page_number).object_list,
            many=True
        )
        pagination_info = PaginatorSerializer(
            paginator=paginator,
            page_number=page_number,
        )
        return Response(
            {
                'data': serializer.data,
                'pagination_info': pagination_info.to_dict()
            }
        )
