from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Facultad, Curso
from .serializers import FacultadSerializer, CursoSerializer


class FacultadViewSet(viewsets.ModelViewSet):
    """
    ViewSet completo para Facultad con soporte CRUD y subida de imágenes.
    """
    queryset = Facultad.objects.all().order_by('-created_at')
    serializer_class = FacultadSerializer
    parser_classes = (MultiPartParser, FormParser)  # permite subir archivos (logo)

    def get_serializer_context(self):
        """
        Permite acceder al objeto 'request' en el serializer,
        para construir URLs completas (logo_url).
        """
        return {'request': self.request}


class CursoViewSet(viewsets.ModelViewSet):
    """
    ViewSet completo para Curso con soporte CRUD y subida de imágenes.
    """
    queryset = Curso.objects.all().order_by('-created_at')
    serializer_class = CursoSerializer
    parser_classes = (MultiPartParser, FormParser)  # permite subir archivos (portada)

    def get_serializer_context(self):
        """
        Igual que en FacultadViewSet, pasa 'request' al serializer.
        """
        return {'request': self.request}
