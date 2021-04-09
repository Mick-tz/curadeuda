# utils
from django.core.paginator import Paginator
from sepomex.serializers.paginator_serializer import PaginatorSerializer

# modelos y serializadores del codigo postal
from codigos_postales.models.codigo_postal import CodigoPostal
from codigos_postales.serializers.serializador_codigo_postal import SerializadorCodigoPostal

# manejo de autenticacion y respuesta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CodigoPostalList(APIView):
    """
    View para listar los codigos postales
    """
    # descomentar la siguiente línea cuando se tenga implementado el sistema de usuarios 
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # obtenemos la informacion de la paginación, en caso de no ser provista, el default es de 20 resultados por página
        page_number = int(request.GET['page_number']) if 'page_number' in request.GET else 1
        page_size = int(request.GET['page_size']) if 'page_size' in request.GET else 20

        # el queryset consta de todos los codigos postales
        codigos = CodigoPostal.objects.all()

        # creamos paginator con la cantidad de codigos requerida
        paginator = Paginator(
            object_list=codigos,
            per_page=page_size, 
        )

        # usando el paginator, serializamos los estados requeridos junto a la informacion de paginacion
        serializer = SerializadorCodigoPostal(
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
