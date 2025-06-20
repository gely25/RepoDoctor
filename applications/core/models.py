from django.db import models

# Create your models here.


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    
    
class EspecialidadMedica(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre




class Doctor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.ForeignKey(EspecialidadMedica, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"





class Empleado(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"



class TipoSangre(models.Model):
    tipo = models.CharField(max_length=5)  # Ejemplo: A+, O-, etc.

    def __str__(self):
        return self.tipo





class Paciente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tipo_sangre = models.ForeignKey(TipoSangre, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to='pacientes_fotos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


