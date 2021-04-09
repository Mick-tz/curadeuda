from rest_framework import serializers

from codigos_postales.models.estado import Estado

class SerializadorEstado(serializers.ModelSerializer):

    class Meta:
        model = Estado
        fields = [
            'c_estado',
            'd_estado',
        ]
