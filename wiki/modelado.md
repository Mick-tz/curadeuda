## Modelado

*Todos los modelos heredan de una clase base que simplemente agregar hora de creación y modificación de forma automática*

*Los campos que no permiten repeticiones son procedidos por la palabra "UNIQUE", todo campo de id (claves por consitencia con notación SEPOMEX) no permite repeticiones dentro de su relación*

*Los campos opcionales en los objetos se indican con la palabra "NULL"*

*Todo campo no seguido por la palabra "NULL" es considerado obligatorio*

*Los campos que son procedidos por la palabra "AUTO" serán agregados de forma automática sin la participación del usuario.*

*Los campos que corresponden a un id de otro objeto se siguen de "FK" y las llaves primarias (id) de "PK"*

*OBS: Se utiliza una arquitectura de copo de nieve para la relación entre las tablas.*

```
Estado: {
    """
    Representa un estado de la república, por consistencia, la llave primaria (al igual que el
    resto de los campos) es llamada de igual forma y corresponde al campo c_estado provisto por  
    SEPOMEX.
    """

    c_estado: int,                                          "PK"  
    d_estado: Str   
}

Municipio: {
    """
    Representa un municipio. Por consistencia, la llave primaria (al igual que el
    resto de los campos) es llamada de igual forma y corresponde al campo c_mnpio provisto por  
    SEPOMEX.
    """

    c_mnpio: int,                                         "PK"   
    d_mnpio: Str,
    c_estado: int,                                        "FK"
}

Asentamiento: {
    """
    Representa un asentamiento (e.g. colonia, pueblo, barrio,...). Por consistencia, la llave 
    primaria (al igual que el resto de los campos) es llamada de igual forma y corresponde al
    campo provisto por SEPOMEX (id_asenta_cpcons).
    """

    id_asenta_cpcons: int,                                         "PK"   
    d_asenta: Str,
    d_tipo_asenta: Str,   
    c_tipo_asenta, int
    c_mnpio: int                                                   "FK"
}

CodigoPostal: {
    """
    Representa el codigo postal. Por consistencia, la llave 
    primaria (al igual que el resto de los campos) es llamada de igual forma y corresponde al
    campo provisto por SEPOMEX (d_codigo).
    """

    id: uuid,                                              "PK"
    d_codigo: str,      
    id_asenta_cpcons: int                                  "FK"
}
```

*TODO: implementar el modelado de usuarios y superuser, propuesta a continuación.*

```
Usuario: {
    """
    Modelo generico de usuario.
    """

    id: uuid,                                         "AUTO PK"
    nombre_usuario: Str                               "UNIQUE"
    nombres: Str,
    apellidos: Str,
    telefono: Str,                                    "NULL"
    correo: Email,                                    "NULL"
    password: HashedStr,
    tokens: Array[csrf_tokens]                        "NULL"
}
```
