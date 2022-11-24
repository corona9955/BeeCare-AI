# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib import admin
from django.urls import path, include

# |=========================================|
# |=====|   BIBLIOTECAS ADICIONALES   |=====|
# |=========================================|

# |=| Biblioteca que permite redireccionar|=|
from django.shortcuts import redirect
# |=| Biblioteca que permite personalizar la página de error 404 |=|
from django.conf.urls import handler404

# |=============================================================|
# |===============|        Lista de URLs        |===============|
# |=============================================================|

urlpatterns = [
    # |===============================================|
    # |========| REDIRECCIONAMIENTO DE HOME  |========|
    # |===============================================|
    path('', lambda req: redirect('/memb/')),
    
    # |===============================================|
    # |========|     DIRS. DE TRABAJADORES   |========|
    # |===============================================|
    path('memb/', include('apps.member.urls')),

    # |===============================================|
    # |=============| DIRS. DE SIGHTING |=============|
    # |===============================================|
    path('sighting/', include('apps.sighting.urls')),

    # |===============================================|
    # |=============|   DIRS. DE WIKI   |=============|
    # |===============================================|
    path('wiki/', include('apps.wiki.urls')),
    
    # |===============================================|
    # |========|   DIRS. DE ADMINISTRACIÓN   |========|
    # |===============================================|
    path('admin/', admin.site.urls),
]

handler404 = 'apps.member.views.error404'