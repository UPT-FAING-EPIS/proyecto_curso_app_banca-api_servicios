from django.urls import path, include
from rest_framework import routers
from .views import DeudasAlumnoViews, BuscarDeudores, PagosAlumnoViews
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
    path('listardeudores/<str:fk_codigo_alumno>/', BuscarDeudores.as_view(), name='listar_deudores'),
]
