from django.db import models

class Facultad(models.Model):
    nombre = models.CharField(max_length=200)
    decano = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    logo = models.ImageField(upload_to='facultad_logos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    facultad = models.ForeignKey(Facultad, related_name='cursos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=200)
    horario = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    portada = models.ImageField(upload_to='curso_portadas/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
