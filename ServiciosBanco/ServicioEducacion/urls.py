from django.urls import path
from .views import RealizarPagoView,DeudasAlumnoViews,PagosAlumnoViews

urlpatterns = [
    path('deudas/', DeudasAlumnoViews.as_view(), name='deudas'),
    path('pagos/', PagosAlumnoViews.as_view(), name='pagos'),
    path('pagar/', RealizarPagoView.as_view(), name='realizar_pago'),
]
