from django.urls import path
from .views import PagoListView, DeudaListView

urlpatterns = [
    path('deuda/', DeudaListView.as_view(), name='tb_deuda_list'),
    path('pago/', PagoListView.as_view(), name='tb_pagos_list')
]
