from django.db import models
from datetime import date

# Create your models here.
class tbAlumno(models.Model):
    CodigoAlumno = models.CharField(max_length=255, primary_key=True)
    Nombre = models.CharField(max_length=255)
    Apellido = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    class Meta:
        db_table = "tbAlumno"

class tbDeudasAlumno(models.Model):
    CodigoDeuda = models.AutoField(primary_key=True)
    fkCodigoAlumno = models.ForeignKey(tbAlumno, on_delete=models.CASCADE)
    CantidadDeuda = models.DecimalField(max_digits=10, decimal_places=2)
    FechaVencimiento = models.DateField()
    Estado = models.BooleanField(default=False)
    class Meta:
        db_table = "tbDeudasAlumno"

class tbPagosAlumno(models.Model):
    CodigoPago = models.AutoField(primary_key=True)
    FKCodigoDeuda = models.ForeignKey(tbDeudasAlumno, on_delete=models.CASCADE)
    MontoPago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    FechaPago = models.DateField(default=date.today)
    class Meta:
        db_table = "tbPagosAlumno"

