from django.urls import path
from .views import AlumnoPagoView,AlumnosListView



urlpatterns = [
    path('', AlumnosListView.as_view(), name='alumno-list'),
    path('pago/<int:CodigoAlumno>/', AlumnoPagoView.as_view(), name='alumnos-detail')
]
