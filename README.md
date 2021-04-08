# curadeuda

Para este proyecto es necesario Python 3.x

De preferencia tener virtualenv y generar un environment para manejar las librerias adecuadas de python3

Una vez teniendo activo el virtualenv con python 3 se requiere instalar las librerias del proyecto, ya sea en desarrollo o producción, dentro del directorio `sepomex` de este proyecto, bastará con ejecutar:

`$ pip install -r requirements.txt`

Para poder correr el servidor con informacion basta con correr:

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
