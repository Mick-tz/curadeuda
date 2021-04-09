from django.db import models
from codigos_postales.models.municipio import Municipio
from base.models.modelo_base import ModeloBase


class Asentamiento(ModeloBase):

    id_asenta_cpcons: int = models.IntegerField(primary_key=True)
    d_asenta: str = models.CharField(max_length=256)
    d_tipo_asenta: str = models.CharField(max_length=256)
    c_tipo_asenta: int = models.IntegerField()
    c_mnpio: Municipio = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        help_text="municipio al que pertenece el asentamiento"
    )

    def __str__(self):
        return self.d_asenta

    class Meta:
        ordering = ['id_asenta_cpcons']
        verbose_name = "Asentamiento"
        verbose_name_plural = "Asentamientos"

class AsentamientoFactory:
    """
    Clase para agregar instancias del modelo
    """
    model_class = Asentamiento
    foreign_key_models = {
        'Municipio': Municipio
    }
    def new_instance(
            self,
            id_asenta_cpcons: int,
            d_asenta: str,
            d_tipo_asenta: str,
            c_tipo_asenta: int,
            c_mnpio: int
    ):
        # zona de validaciones
        # e.g. para asegurarnos que no existe un estado previamente con dicho
        # assert self.model_class.objects.get(id_asenta_cpcons=id_asenta_cpcons) == None

        # TODO: agregar validaciones a validators de los fields en el modelo, 
        # si se quedan solo ahi, entonces el error lo dara a la hora de hacer el bulk_save y si hay rollback no guardara nada

        municipio = self.foreign_key_models['Municipio'].objects.get(c_mnpio=c_mnpio)
        return self.model_class(
            id_asenta_cpcons = id_asenta_cpcons,
            d_asenta = d_asenta,
            d_tipo_asenta = d_tipo_asenta,
            c_tipo_asenta = c_tipo_asenta,
            c_mnpio = municipio
        )