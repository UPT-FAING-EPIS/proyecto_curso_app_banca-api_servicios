from rest_framework import generics
from rest_framework.response import Response
from .models import CuentAlumnos
from .serializers import AlumnosSerializer

class AlumnosListView(generics.ListCreateAPIView):
    queryset = CuentAlumnos.objects.all()
    serializer_class = AlumnosSerializer

class AlumnoPagoView(generics.RetrieveUpdateAPIView):
    queryset = CuentAlumnos.objects.all()
    serializer_class = AlumnosSerializer
    lookup_field = 'CodigoAlumno'

    def patch(self, request, *args, **kwargs):
        monto_pago = request.data.get('MontoPago')
        if not monto_pago:
            return Response({'error': 'Falta el valor de MontoPago'}, status=400)
        monto_pago = float(monto_pago)
        alumno = self.get_object()
        if monto_pago > alumno.MontoDeuda:
            return Response({'mensaje': 'El monto es demasiado'}, status=400)
        elif monto_pago < alumno.MontoDeuda:
            return Response({'mensaje': 'El monto de pago es insuficiente'}, status=400)
        alumno.MontoDeuda = 0
        alumno.MontoPago = 0
        alumno.save()
        serializer = self.get_serializer(alumno)
        response_data = {'mensaje': 'Pago Realizado', 'data': serializer.data}
        return Response(response_data, status=200)
