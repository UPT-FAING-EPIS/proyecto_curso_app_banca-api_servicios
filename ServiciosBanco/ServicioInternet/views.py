from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import CuentDeudInter
from .serializers import DeudInterSerializer,DeudInterSerializer2
from datetime import datetime

class DeudInterListView(viewsets.ModelViewSet):
    serializer_class = DeudInterSerializer
    queryset = CuentDeudInter.objects.all()


class DeudInterPagoView(generics.RetrieveUpdateAPIView):
    queryset = CuentDeudInter.objects.all()
    serializer_class = DeudInterSerializer2
    lookup_field = 'CodigoDeudInter'
    http_method_names = ['get', 'patch']

    def patch(self, request, *args, **kwargs):
        pago = request.data.get('MonPago')
        boldeuda=False
        if not pago:
            return Response({'error': 'Falta el valor en MonPago'}, status=400)

        DeudInter = self.get_object()

        if datetime.date(datetime.now()) > DeudInter.FechVenc:
            pago=float(pago)-5.00
            boldeuda=True
        

        if (float(pago) >= DeudInter.MonDeuda) or (float(pago) <0):
            return Response({'mensaje': 'El Pago no es el debido'}, status=400)
        
        DeudInter.MonDeuda = float(float(DeudInter.MonDeuda)-float(pago))

        DeudInter.save()

        serializer = self.get_serializer(DeudInter)
        if boldeuda:
            response_data = {'mensaje': 'Pago Realizado con extra de mora 50', 'data': serializer.data}
        response_data = {'mensaje': 'Pago Realizado', 'data': serializer.data}
        return Response(response_data, status=200)
