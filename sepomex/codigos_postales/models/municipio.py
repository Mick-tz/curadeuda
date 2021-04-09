# modelos
from django.db import models
from codigos_postales.models.estado import Estado
from base.models.modelo_base import ModeloBase


class Municipio(ModeloBase):

    c_mnpio: int = models.IntegerField(primary_key=True)
    d_mnpio: str = models.CharField(max_length=256)
    c_estado: Estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        help_text="estado al que pertenece el municipio"
    )

    def __str__(self):
        return self.d_mnpio

    class Meta:
        ordering = ['c_mnpio']
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

class MunicipioFactory:
    """
    Clase para agregar instancias del modelo
    """
    model_class = Municipio
    foreign_key_models = {
        'Estado': Estado
    }
    def new_instance(
            self,
            c_mnpio: int,
            d_mnpio: str,
            c_estado: int
    ):
        # zona de validaciones
        # e.g. para asegurarnos que no existe un estado previamente con dicho
        # assert self.model_class.objects.get(c_mnpio=c_mnpio) == None

        # TODO: agregar validaciones a validators de los fields en el modelo, 
        # si se quedan solo ahi, entonces el error lo dara a la hora de hacer el bulk_save y si hay rollback no guardara nada

        estado = self.foreign_key_models['Estado'].objects.get(c_estado=c_estado)
        return self.model_class(
            c_mnpio = c_mnpio,
            d_mnpio = d_mnpio,
            c_estado = estado
        )