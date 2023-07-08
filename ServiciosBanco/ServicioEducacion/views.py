from rest_framework.exceptions import NotFound
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import tbAlumno, tbDeudasAlumno, tbPagosAlumno
from .serializers import tbAlumnoSerializer, tbDeudasAlumnoSerializer, tbPagosAlumnoSerializer
from django.shortcuts import get_object_or_404


class AlumnoViews(viewsets.ModelViewSet):
    queryset = tbAlumno.objects.using('BaseDatosEducacion').all()
    serializer_class = tbAlumnoSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class DeudasAlumnoViews(viewsets.ModelViewSet):
    queryset = tbDeudasAlumno.objects.using('BaseDatosEducacion').all()
    serializer_class = tbDeudasAlumnoSerializer
    permission_classes = [permissions.AllowAny]

    def search_by_dni(self, dni):
        queryset = self.queryset.filter(fkCodigoAlumno=dni)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()


class PagosAlumnoViews(viewsets.ModelViewSet):
    queryset = tbPagosAlumno.objects.using('BaseDatosEducacion').all()
    serializer_class = tbPagosAlumnoSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class BuscarDeudores(APIView):
    def get(self, request, fk_codigo_alumno):
        alumno = get_object_or_404(tbAlumno.objects.using(
            'BaseDatosEducacion'), CodigoAlumno=fk_codigo_alumno)

        deudas = tbDeudasAlumno.objects.using('BaseDatosEducacion').filter(
            fkCodigoAlumno__CodigoAlumno=fk_codigo_alumno)
        serializer = tbDeudasAlumnoSerializer(deudas, many=True)

        response_data = []
        for deuda in serializer.data:
            if deuda['Estado'] == 0:
                deuda['Situacion'] = 'Pendiente'
            else:
                deuda['Situacion'] = 'Pagado'
            response_data.append(deuda)

        if not response_data:
            raise NotFound('Alumno no encontrado')

        return Response(response_data)

    def perform_create(self, serializer):
        serializer.save()
