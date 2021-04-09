# utils
from django.core.paginator import Paginator
from sepomex.serializers.paginator_serializer import PaginatorSerializer

# modelos y serializadores de estado
from codigos_postales.models.estado import Estado
from codigos_postales.serializers.serializador_estado import SerializadorEstado

# manejo de autenticacion y respuesta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from rest_framework import status

class EstadoList(APIView):
    """
    View para listar los estados
    """
    # descomentar la siguiente línea cuando se tenga implementado el sistema de usuarios 
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # obtenemos la informacion de la paginación, en caso de no ser provista, respondemos con la información completa, dado que sólo son 32 estados.
        # TODO: discutir query string required o no
        page_number = int(request.GET['page_number']) if 'page_number' in request.GET else 1
        page_size = int(request.GET['page_size']) if 'page_size' in request.GET else 32
        
        # el queryset consta de todos los estados
        estados = Estado.objects.all() if not 'd_estado' in request.GET else Estado.objects.filter(d_estado__icontains=request.GET['d_estado'])

        # creamos paginator con la cantidad de estados requerida
        paginator = Paginator(
            object_list=estados,
            per_page=page_size, 
        )

        # usando el paginator, serializamos los estados requeridos junto a la informacion de paginacion
        serializer = SerializadorEstado(
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

    def post(self, request, format=None):
        serializer = SerializadorEstado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'estado': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
