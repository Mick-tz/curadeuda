from django.db import models


class ModeloBase(models.Model):
    """
    Modelo Abstracto (No existe tabla)
    Contiene informacion que deben tener todos los modelos

    fecha_creacion: cuando se crea el modelo
    fecha_ultima_modificacion: la ultima vez que se modifico el objeto
    """
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
