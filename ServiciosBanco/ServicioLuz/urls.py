from django.urls import path,include
from .views import DeudaListView,DeudaDetailView,PagoListView,PagosDetailView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('deudas', DeudaListView)


urlpatterns = [
    path('deudas/', DeudaListView.as_view(), name='deuda-list'),
    path('deudas/<int:pk>/', DeudaDetailView.as_view(), name='deuda-detail'),
    path('pagos/', PagoListView.as_view(), name='pagos-list'),
    path('pagos/<int:pk>/', PagosDetailView.as_view(), name='pago-detail'),
]
