from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api_recibos_agua import views


urlpatterns = [
    path('deuda/<str:codigo_cliente>/', views.get_deuda, name='get_deuda'),
    
   
]
