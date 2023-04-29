from rest_framework import serializers
from .models import tbAlumno, tbDeudasAlumno, tbPagosAlumno

class tbAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbAlumno
        fields = '__all__'

class tbDeudasAlumnoSerializer(serializers.ModelSerializer):
    fkCodigoAlumno = serializers.PrimaryKeyRelatedField(queryset=tbAlumno.objects.all())
    class Meta:
        model = tbDeudasAlumno
        fields = '__all__'

class tbPagosAlumnoSerializer(serializers.ModelSerializer):
    FKCodigoDeuda = serializers.PrimaryKeyRelatedField(queryset=tbDeudasAlumno.objects.all())
    class Meta:
        model = tbPagosAlumno
        fields = '__all__'
