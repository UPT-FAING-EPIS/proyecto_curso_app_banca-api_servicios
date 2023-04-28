from rest_framework import serializers
from .models import CuentAlumnos

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentAlumnos
        fields = ('CodigoAlumno', 'Nombre', 'Apellido', 'FechaVencimientoPago', 'MontoDeuda', 'MontoPago', 'Estado')
        read_only_fields = ('Estado',)
