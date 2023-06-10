from django.urls import path
from .views import DeudaListView, DeudaDetailView, PagoListView, PagoDetailView

urlpatterns = [
    path('deudas/', DeudaListView.as_view(), name='deuda-list'),
    path('deudas/<int:pk>/', DeudaDetailView.as_view(), name='deuda-detail'),
    path('pagos/', PagoListView.as_view(), name='pago-list'),
    path('pagos/<int:pk>/', PagoDetailView.as_view(), name='pago-detail'),
]
