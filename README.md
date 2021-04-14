# curadeuda

Para este proyecto es necesario Python 3.x

OBS: todo path mencionado es relativo a la raíz del proyecto.

De preferencia tener virtualenv y generar un environment para manejar las librerias adecuadas de python3

Una vez teniendo activo el virtualenv con python 3 se requiere instalar las librerias del proyecto, ya sea en desarrollo o producción, dentro del directorio raiz de este proyecto, bastará con ejecutar:

`$ pip install -r requirements.txt`

Antes de cargar la información, asegurate que el archivo "raw/CPdescargatxt/CPdescarga.txt" esté recidente y cumpla las especificaciones esperadas (la primera línea debe coincidir con el header, debe usar el símbolo "|" como separador de valores; la primera linea contendrá los nombres de los campos, de los cuales al menos se debe incluir: d_codigo, c_estado, d_estado, d_asenta, d_tipo_asenta, D_mnpio, id_asenta_cpcons, c_tipo_asenta y c_mnpio de acuerdo a lo descrito en "wiki/Descripcion.pdf"), si no estás seguro de esto, puedes apoyarte de los scripts de bash contenidos en el directorio "scripts/" (sh scripts/script_name.sh)

Si es la primera vez que ejecutas los scripts de bash, no olvides asegurarte que tengan permiso de ejecución (en caso contrario ejecuta "chmod +x scripts/script_name.sh" antes de correr el script).

OBS: Contrario a lo que se menciona en el archivo provisto por sepomex ("wiki/Descripcion.pdf"), el campo "id_asenta_cpcons" no es único (por la descripción, pareciera que debería ser el campo clave del asentamiento). De esta form, el script "scripts/prepare_raw_file.sh" lo único que hará (al momento) es modificar dicho campo para que convertirlos enteros positivos sin repeticiones.

IMPORTANTE: El resultado de los scripts sólo es valido si se encuentran en la dirección esperada ("scripts/").

Para poder correr el servidor con informacion basta con moverse al directorio `sepomex` y correr los siguientes comandos:

`$ python manage.py makemigrations && python manage.py migrate && python manage.py filldatabase`

Para poder acceder a la vista de admin es necesario crear un superuser corriendo:

`$ python manage.py createsuperuser`

Para correr el server basta con correr:

`$ python manage.py runserver`

En desarrollo, para poder acceder a la vista de admin se basta con entrar a [localhost:8000/admin](http://localhost:8000/) en tu navegador, la configuración para producción requiere seguir una serie de pasos distintos.

Se recomiendan los siguientes artículos (actualizado en abril 8 del 2021) si el deployment se lleva a cabo en

heroku:

[django-deploy-heroku](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43)

y en digital ocean:

[diango-deploy-digital-ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps)

Si el deployment se lleva a cabo en alguna otra plataforma, consultar con el administrador.

Cualquier duda contactar a alguno de los correos:

> [miguel.martinez@ciencias.unam.mx](mailto:miguel.martinez@ciencias.unam.mx)
> 

La versión alfa se puede encontrar en:
> [alfa](https://prueba-sepomex-alfa.herokuapp.com/api/estados) 
> 

Naturalmente, hay que navegar entre endpoints de acuerdo a wiki/endpoints.md contactar a [miguel.martinez@ciencias.unam.mx](mailto:miguel.martinez@ciencias.unam.mx) para solicitar un usuario del admin en la versión alfa.
