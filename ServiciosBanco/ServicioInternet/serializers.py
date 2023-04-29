from rest_framework import serializers
from .models import CuentDeudInter

class DeudInterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentDeudInter
        fields = '__all__'
        read_only_fields = ('Estado','MonPago')
