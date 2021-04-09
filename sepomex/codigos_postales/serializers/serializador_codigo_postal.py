from rest_framework import serializers

from codigos_postales.serializers.serializador_asentamiento import SerializadorAsentamiento
from codigos_postales.models.codigo_postal import CodigoPostal


class SerializadorCodigoPostal(serializers.ModelSerializer):
    id_asenta_cpcons = SerializadorAsentamiento(read_only=True)


    class Meta:
        model = CodigoPostal
        fields = [
            # 'id', # TODO: DISCUSS
            'd_codigo',
            'id_asenta_cpcons',
        ]
