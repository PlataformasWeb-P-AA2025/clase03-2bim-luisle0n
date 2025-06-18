from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=30)
    capital= models.CharField(max_length=30)
    numeroProvincia = models.IntegerField()
    numeroHabitantes = models.IntegerField()


    # capital
    # número de provincias
    # número de habitantes
    def __str__(self):
        return "%s %s %d %d" % (self.nombre,
                    self.capital,
                    self.numeroProvincia,
                    self.numeroHabitantes)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.apellido,
                self.cedula)

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
