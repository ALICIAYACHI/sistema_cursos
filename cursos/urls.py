from rest_framework import routers
from django.urls import path, include
from .views import FacultadViewSet, CursoViewSet

router = routers.DefaultRouter()
router.register(r'facultades', FacultadViewSet)
router.register(r'cursos', CursoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
