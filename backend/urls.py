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
    Vista raíz de la API.
    Muestra un mensaje simple para confirmar que el backend funciona.
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
    path('api/', include('cursos.urls')),  # ✅ rutas de la app cursos
    path('', home, name='home'),           # 👈 raíz informativa
]

# ✅ Servir archivos media en desarrollo y Render
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
