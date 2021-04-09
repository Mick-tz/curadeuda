import uuid

from django.db import models
from codigos_postales.models.asentamiento import Asentamiento
from base.models.modelo_base import ModeloBase


class CodigoPostal(ModeloBase):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    d_codigo: str = models.CharField(max_length=256)
    id_asenta_cpcons: Asentamiento = models.ForeignKey(
        Asentamiento,
        on_delete=models.CASCADE,
        help_text="asentamiento al que pertenece el código postal"
    )

    def __str__(self):
        return self.d_codigo

    class Meta:
        ordering = ['id']
        verbose_name = "Codigo postal"
        verbose_name_plural = "Codigos postales"

class CodigoPostalFactory:
    """
    Clase para agregar instancias del modelo
    """
    model_class = CodigoPostal
    foreign_key_models = {
        'Asentamiento': Asentamiento
    }
    def new_instance(
            self,
            d_codigo: str,
            id_asenta_cpcons: int
    ):
        # zona de validaciones
        # e.g. para asegurarnos que no existe un estado previamente con dicho
        # assert self.model_class.objects.get(id_asenta_cpcons=id_asenta_cpcons) == None

        # TODO: agregar validaciones a validators de los fields en el modelo, 
        # si se quedan solo ahi, entonces el error lo dara a la hora de hacer el bulk_save y si hay rollback no guardara nada

        asentamiento = self.foreign_key_models['Asentamiento'].objects.get(id_asenta_cpcons=id_asenta_cpcons)
        return self.model_class(
            d_codigo = d_codigo,
            id_asenta_cpcons = asentamiento
        )