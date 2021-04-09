# modelos
from django.db import models
from base.models.modelo_base import ModeloBase


class Estado(ModeloBase):

    c_estado: int = models.IntegerField(primary_key=True)
    d_estado: str = models.CharField(max_length=64, unique=True, db_index=True)

    def __str__(self):
        return self.d_estado

    class Meta:
        ordering = ['c_estado']
        verbose_name = "Estado de la república"
        verbose_name_plural = "Estados de la república"

class EstadoFactory:
    """
    Clase para agregar instancias del modelo
    """
    model_class = Estado
    def new_instance(
            self,
            c_estado: int,
            d_estado: str,
    ):
        # zona de validaciones
        # e.g. para asegurarnos que no existe un estado previamente con dicho
        # assert self.model_class.objects.get(c_estado=c_estado) == None
        if self.model_class.objects.filter(c_estado=c_estado):
            return self.model_class.objects.get(c_estado=c_estado)

        # TODO: agregar validaciones a validators de los fields en el modelo, 
        # si se quedan solo ahi, entonces el error lo dara a la hora de hacer el bulk_save y si hay rollback no guardara nada

        return self.model_class(
            c_estado = c_estado,
            d_estado = d_estado,
        )