# utils
from django.core.paginator import Paginator
from sepomex.serializers.paginator_serializer import PaginatorSerializer

# modelos y serializadores de estado
from codigos_postales.models.municipio import Municipio
from codigos_postales.serializers.serializador_municipio import SerializadorMunicipio
from codigos_postales.models.estado import Estado

# manejo de autenticacion y respuesta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
class MunicipioList(APIView):
    """
    View para listar los municipios
    """
    # descomentar la siguiente línea cuando se tenga implementado el sistema de usuarios 
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # obtenemos la informacion de la paginación, el default de page_size será 20
        page_number = int(request.GET['page_number']) if 'page_number' in request.GET else 1
        page_size = int(request.GET['page_size']) if 'page_size' in request.GET else 20
        
        # el queryset consta de todos los municipios si no se provee el nombre parcial
        municipios = Municipio.objects.all() if not 'd_mnpio' in request.GET else Municipio.objects.filter(d_mnpio__icontains=request.GET['d_mnpio'])

        # creamos paginator con la cantidad de municipios requerida
        paginator = Paginator(
            object_list=municipios,
            per_page=page_size, 
        )

        # usando el paginator, serializamos los municipios requeridos junto a la informacion de paginacion
        serializer = SerializadorMunicipio(
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
        estado = Estado.objects.get(c_estado=request.data['c_estado'])
        serializer = SerializadorMunicipio(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['c_estado'] = estado
            serializer.save()
            return Response({'municipio': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)