from rest_framework import serializers
from .models import TbPagos
from .models import TbDeuda
from .models import TbClientes
 
class PagosSerializer(serializers.ModelSerializer):
    CodigoDeuda_id = serializers.PrimaryKeyRelatedField(queryset=TbDeuda.objects.all())
    class Meta:
        model = TbPagos
        fields = '__all__'
     
class DeudaSerializer(serializers.ModelSerializer):
    FkCodigoCliente = serializers.PrimaryKeyRelatedField(queryset=TbClientes.objects.all())
    class Meta:
        model = TbDeuda
        fields = '__all__'
      