from rest_framework import serializers

from codigos_postales.serializers.serializador_estado import SerializadorEstado
from codigos_postales.models.municipio import Municipio


class SerializadorMunicipio(serializers.ModelSerializer):
    c_estado = SerializadorEstado(read_only=True)

    class Meta:
        model = Municipio
        fields = [
            'c_mnpio',
            'd_mnpio',
            'c_estado',
        ]
