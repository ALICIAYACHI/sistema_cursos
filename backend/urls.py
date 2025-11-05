"""
URL configuration for backend project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse


def home(request):
    """
    Vista raíz simple para comprobar conexión con la API.
    """
    return JsonResponse({
        "message": "Bienvenido a la API del Sistema de Cursos 🎓",
        "status": "online",
        "endpoints": [
            "/api/facultades/",
            "/api/cursos/"
        ]
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cursos.urls')),
    path('', home, name='home'),
]

# Servir archivos media en desarrollo y producción (Render)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
