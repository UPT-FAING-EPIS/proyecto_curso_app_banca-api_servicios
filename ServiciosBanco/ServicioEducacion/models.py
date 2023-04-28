from django.db import models

# Create your models here.
class CuentAlumnos(models.Model):
    CodigoAlumno = models.CharField(max_length=255,primary_key=True)
    Nombre = models.CharField(max_length=255)
    Apellido = models.CharField(max_length=255)
    MontoDeuda = models.DecimalField(max_digits=10, decimal_places=2)
    MontoPago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    FechaVencimientoPago = models.DateField()
    Estado = models.BooleanField(default=False)
    class Meta:
        db_table = "CuentAlumnos"