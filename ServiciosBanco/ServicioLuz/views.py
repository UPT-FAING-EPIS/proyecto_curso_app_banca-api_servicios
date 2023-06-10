from rest_framework import generics
from rest_framework.response import Response
from .models import TbPagos
from.models import TbDeuda
from .serializers import DeudaSerializer, PagosSerializer
from datetime import datetime


class DeudaListView(generics.ListCreateAPIView):
    queryset = TbDeuda.objects.all()
    serializer_class = DeudaSerializer

class PagoListView(generics.ListCreateAPIView):
    queryset = TbPagos.objects.all()
    serializer_class = PagosSerializer
    
    def post(self, request, *args, **kwargs):
        codigo_deuda = request.data.get('CodigoDeuda', None)
        if codigo_deuda is None:
            return Response({'error': 'El campo CodigoDeuda es requerido.'}, status=400)
        
        deuda = TbDeuda.objects.filter(CodigoDeuda=codigo_deuda).first()
        if deuda is None:
            return Response({'error': f'La deuda con CodigoDeuda={codigo_deuda} no existe.'}, status=400)
        
        monto_pago = float(request.data.get('Pago', 0))
        fecha_pago_str = request.data.get('FechaPago', datetime.now())
        fecha_pago = datetime.strptime(fecha_pago_str, '%Y-%m-%d').date()

        if deuda.FechaVencimientoPago != fecha_pago:
            deuda.Monto += 80
            deuda.save()
            return Response({'mensaje': 'La fecha de pago y vencimiento no coinciden. Se agregaron S/80 a la deuda.'})

        if monto_pago != deuda.Monto:
            return Response({'error': 'El monto de pago no coincide con la deuda. Se interrumpe la operación.'}, status=400)

        pago = TbPagos(CodigoDeuda=deuda, Pago=monto_pago, FechaPago=fecha_pago)
        pago.save()
        deuda.Estado = 'pagado'
        deuda.save()

        serializer = self.get_serializer(pago)
        response_data = {'mensaje': 'Pago Realizado', 'data': serializer.data}
        return Response(response_data, status=200)

