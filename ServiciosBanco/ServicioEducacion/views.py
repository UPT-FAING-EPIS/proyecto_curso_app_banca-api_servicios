from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import tbDeudasAlumno, tbPagosAlumno
from .serializers import tbDeudasAlumnoSerializer, tbPagosAlumnoSerializer

from django.shortcuts import render
import requests


class DeudasAlumnoViews(viewsets.ModelViewSet):
    queryset = tbDeudasAlumno.objects.all()
    serializer_class = tbDeudasAlumnoSerializer
    permission_classes = [permissions.AllowAny]

class PagosAlumnoViews(viewsets.ModelViewSet):
    queryset = tbPagosAlumno.objects.all()
    serializer_class = tbPagosAlumnoSerializer
    permission_classes = [permissions.AllowAny]


def lista_elementos(request):
    response = requests.get('http://127.0.0.1:8000/ServicioEducacion/deudas/')  # Ejemplo de URL de la API
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa
        elementos = response.json()  # Convierte la respuesta JSON en un diccionario o lista Python
        return render(request, 'deudores.html', {'elementos': elementos})
    else:
        # Maneja el error en caso de que la solicitud no sea exitosa
        return render(request, 'error.html', {'mensaje': 'No se pudo obtener los elementos'})
