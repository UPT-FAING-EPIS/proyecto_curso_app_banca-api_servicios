from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import tbDeudasAlumno, tbPagosAlumno
from .serializers import tbPagosAlumnoSerializer, tbDeudasAlumnoSerializer


class DeudasAlumnoViews(ListCreateAPIView):
    queryset = tbDeudasAlumno.objects.all()
    serializer_class = tbDeudasAlumnoSerializer
    lookup_field = 'CodigoDeuda'


class PagosAlumnoViews(ListCreateAPIView):
    queryset = tbPagosAlumno.objects.all()
    serializer_class = tbPagosAlumnoSerializer


class RealizarPagoView(APIView):
    def post(self, request):
        codigo_deuda = request.data.get('CodigoDeuda')
        monto_pago = request.data.get('MontoPago')
        deuda = get_object_or_404(tbDeudasAlumno, CodigoDeuda=codigo_deuda)
        return self.realizar_pago(deuda, monto_pago)

    def realizar_pago(self, deuda, monto_pago):
        if deuda.Estado:
            return Response({'mensaje': 'La deuda ya ha sido pagada.'}, status=status.HTTP_400_BAD_REQUEST)

        if monto_pago != deuda.CantidadDeuda:
            return Response({'mensaje': 'El monto del pago no es igual a la cantidad de la deuda.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = tbPagosAlumnoSerializer(data={'FKCodigoDeuda': deuda.CodigoDeuda, 'MontoPago': monto_pago})
        if serializer.is_valid():
            serializer.save()
            deuda.Estado = True
            deuda.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
