from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import CuentDeudInter
from .serializers import DeudInterSerializer, DeudInterSerializer2
from datetime import datetime
from decimal import Decimal
from ..ServiciosBanco.factory import DeudInterPagoFactory


class DeudInterListView(viewsets.ModelViewSet):
    serializer_class = DeudInterSerializer
    queryset = CuentDeudInter.objects.all()



class DeudInterPagoView(generics.RetrieveUpdateAPIView):
    queryset = CuentDeudInter.objects.all()
    serializer_class = DeudInterSerializer2

    lookup_field = 'CodigoDeudInter'
    http_method_names = ['get', 'patch']

    def patch(self, request, *args, **kwargs):
        pago = Decimal(request.data.get('MonPago'))
        if not pago:
            return Response({'error': 'Falta el valor en Monto Pago'}, status=400)
        
        factoria= DeudInterPagoFactory.create("ServicioInternet",pago)
        deud_inter = self.get_object()
        result = factoria.pagar()
 
        if result['status'] == 200:
            serializer = self.get_serializer(deud_inter)
            response_data = {
                'mensaje': result['mensaje'], 'data': serializer.data}
        else:
            response_data = {'mensaje': result['mensaje']}

        return Response(response_data, status=result['status'])
