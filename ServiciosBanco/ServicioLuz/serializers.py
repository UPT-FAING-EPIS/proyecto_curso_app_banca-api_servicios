from rest_framework import serializers
from .models import TbPagos
from .models import TbDeuda
from .models import TbClientes
 
class PagosSerializer(serializers.ModelSerializer):
    CodigoDeuda_id = serializers.PrimaryKeyRelatedField(queryset=TbDeuda.objects.all())
    class Meta:
        model = TbPagos
        fields = ('CodigoPago','Pago', 'FechaPago' ,'CodigoDeuda_id')
     
class DeudaSerializer(serializers.ModelSerializer):
    CodigoCliente_id = serializers.PrimaryKeyRelatedField(queryset=TbClientes.objects.all())
    class Meta:
        model = TbDeuda
        fields = ('CodigoDeuda','FechaVencimientoPago','Monto','Estado', 'CodigoCliente_id')
      