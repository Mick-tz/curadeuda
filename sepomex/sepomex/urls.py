from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/',
        include('codigos_postales.urls.api_codigos_postales_urls'),
    ),
]
