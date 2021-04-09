from rest_framework import serializers

from codigos_postales.serializers.serializador_municipio import SerializadorMunicipio
from codigos_postales.models.asentamiento import Asentamiento


class SerializadorAsentamiento(serializers.ModelSerializer):
    c_mnpio = SerializadorMunicipio(read_only=True)

    class Meta:
        model = Asentamiento
        fields = [
            'id_asenta_cpcons',
            'd_asenta',
            'd_tipo_asenta',
            'c_tipo_asenta',
            'c_mnpio'
        ]
