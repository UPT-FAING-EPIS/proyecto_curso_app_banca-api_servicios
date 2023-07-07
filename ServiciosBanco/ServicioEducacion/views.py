from rest_framework.exceptions import NotFound
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import tbAlumno, tbDeudasAlumno, tbPagosAlumno
from .serializers import tbDeudasAlumnoSerializer, tbPagosAlumnoSerializer

from django.shortcuts import get_object_or_404, render
import requests
from django.views import View


class DeudasAlumnoViews(viewsets.ModelViewSet):
    queryset = tbDeudasAlumno.objects.all()
    serializer_class = tbDeudasAlumnoSerializer
    permission_classes = [permissions.AllowAny]
    def search_by_dni(self, dni):
            queryset = self.queryset.filter(fkCodigoAlumno=dni)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        
class PagosAlumnoViews(viewsets.ModelViewSet):
    queryset = tbPagosAlumno.objects.all()
    serializer_class = tbPagosAlumnoSerializer
    permission_classes = [permissions.AllowAny]


class BuscarDeudores(APIView):
    def get(self, request, fk_codigo_alumno):
        alumno = get_object_or_404(tbAlumno, CodigoAlumno=fk_codigo_alumno)
        
        deudas = tbDeudasAlumno.objects.filter(fkCodigoAlumno__CodigoAlumno=fk_codigo_alumno)
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