from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class Area(models.Model):

    area = models.CharField(
        max_length=50, verbose_name='Área de la vacante')

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"
        ordering = ['area']
        db_table = "areas_vacante"

    def __str__(self):
        return f"{self.area}"


class Vacante(models.Model):
    nombreVacante = models.CharField(
        max_length=200, verbose_name='Nombre de la vacante')
    nombreEmpresa = models.CharField(
        max_length=200, verbose_name='Nombre de la empresa')

    nivelVacante = models.CharField(
        max_length=200, verbose_name='Nivel de la vacante')

    carreras_afinVacante = models.TextField(verbose_name='Carreras afines')

    area = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)

    descripcion = models.TextField(
        verbose_name='Descripción breve de la vacante')

    actividades = models.TextField(verbose_name='Actividades de la vacante')

    sueldo = models.CharField(
        max_length=50, verbose_name='Sueldo de la vacante')

    email = models.EmailField(verbose_name='Correo de la empresa')

    opcionesGenero = [
        ("Ambos", "Ambos"),
        ("Femenino", "Femenino"),
        ("Hombre", "Hombre")
    ]
    genero = models.CharField(
        max_length=10, verbose_name="Género", choices=opcionesGenero)
    experiencia = models.TextField(verbose_name="Área de experiencia")

    slug = models.SlugField(unique=True, blank=True)

    visible = models.BooleanField(verbose_name='¿Disponible?', default=False)

    horario = models.CharField(
        max_length=50, verbose_name='Horario', default=None)

    nombreContacto = models.CharField(
        max_length=50, verbose_name="Nombre del contacto")

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    def createSlug(self):
        if not self.slug:
            self.slug = slugify(self.nombreEmpresa + self.nombreVacante)
        super(Vacante, self).save()

    class Meta:
        verbose_name = "Vacante"
        verbose_name_plural = "Vacantes"
        db_table = "vacante"
        ordering = ['creado']

    def __str__(self) -> str:
        return f"{self.nombreVacante} | {self.nombreEmpresa}"


class Perfil(models.Model):

    nombre = models.CharField(max_length=100)
    carreras = models.TextField(verbose_name="Carrera afín")
    opcionesGenero = [
        ("Femenino", "Femenino"),
        ("Hombre", "Hombre")
    ]
    genero = models.CharField(
        max_length=20, verbose_name="Género", choices=opcionesGenero)
    experiencia = models.TextField(verbose_name="Experiencia")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        db_table = "perfiles"

    def __str__(self):
        return "{nombre} | {carrera} | {genero}".format(nombre=self.nombre, carrera=self.carreras, genero=self.genero)

class Postulados(models.Model):

    usuario = models.CharField(verbose_name="Usuario", max_length=20)
    vacante = models.CharField(verbose_name="Vacante postulada", max_length=50)
    postulado = models.DateTimeField(verbose_name="Postulado:", auto_now_add=True)

    class Meta:
        verbose_name = "Postulado"
        verbose_name_plural = "Postulados"
        db_table = "postulados"
        ordering = ['postulado']
    
    def __str__(self) -> str:
        return f'{self.usuario} vacante postulada {self.vacante}'

class Image(models.Model):
    nombre = models.CharField(verbose_name="Nombre del logo", max_length=20)
    logo = models.ImageField(verbose_name="Logo")
    visibiliy = models.BooleanField(verbose_name="Mostrar logo", default=False)
    asignado = models.DateTimeField(verbose_name="Asignado", auto_now_add=True)

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logos"
        db_table = "Logos"
        ordering = ['asignado']

    def __str__(self) -> str:
        return f" Logo | {self.nombre}"
