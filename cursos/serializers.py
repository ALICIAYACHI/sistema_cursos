from rest_framework import serializers
from .models import Facultad, Curso


class FacultadSerializer(serializers.ModelSerializer):
    # Campo adicional para mostrar la URL completa de la imagen (logo)
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Facultad
        fields = '__all__'  # incluye todos los campos del modelo
        read_only_fields = ('id', 'created_at')

    def get_logo_url(self, obj):
        """
        Devuelve la URL completa de la imagen (logo), si existe.
        Esto facilita que el frontend pueda mostrarla directamente.
        """
        request = self.context.get('request')
        if obj.logo and hasattr(obj.logo, 'url'):
            return request.build_absolute_uri(obj.logo.url) if request else obj.logo.url
        return None


class CursoSerializer(serializers.ModelSerializer):
    # Mostrar el nombre de la facultad (además del id)
    facultad_nombre = serializers.CharField(source='facultad.nombre', read_only=True)
    portada_url = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

    def get_portada_url(self, obj):
        """
        Devuelve la URL completa de la portada del curso, si existe.
        """
        request = self.context.get('request')
        if obj.portada and hasattr(obj.portada, 'url'):
            return request.build_absolute_uri(obj.portada.url) if request else obj.portada.url
        return None
