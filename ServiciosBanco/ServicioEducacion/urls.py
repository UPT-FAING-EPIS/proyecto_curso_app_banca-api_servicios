from django.urls import path, include
from rest_framework import routers
from .views import DeudasAlumnoViews, ListaDeudoresView, PagosAlumnoViews
from .pagardecorator import RealizarPagoViews
from .pagodebito import PagoDebitoViews

from django.urls import path

router = routers.DefaultRouter()
router.register('deudas', DeudasAlumnoViews)
router.register('pagos', PagosAlumnoViews)

urlpatterns = [
    path('', include(router.urls)),
    path('pagar/', RealizarPagoViews.as_view(), name='realizar_pago'),
    path('pagarDebito/', PagoDebitoViews.as_view(), name='realizar_pago2'),
    path('listardeudores/', ListaDeudoresView.as_view(), name='lista_elementos'),
]


# [
#     path('deudas/', DeudasAlumnoViews.as_view(), name='deudas'),
#     path('pagos/', PagosAlumnoViews.as_view(), name='pagos'),
#     path('pagar/', RealizarPagoView.as_view(), name='realizar_pago'),
# ]
