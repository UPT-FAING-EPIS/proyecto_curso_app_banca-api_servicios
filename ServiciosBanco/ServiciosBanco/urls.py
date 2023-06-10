from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from post.api.router import router_posts
from post.api.views import ClienteViewSet
from post.api.views import crear_plan_con_factura,pagar_factura
from django.contrib import admin



schema_view = get_schema_view(
   openapi.Info(
      title="SERVICIOS DE BANCA",
      default_version='v1',
      description="Integrantes:",
      terms_of_service="",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ServicioTelefonia/', include(router_posts.urls)),
    path('clientes/<int:pk>/cancelar_servicio/', ClienteViewSet.as_view({'put': 'cancelar_servicio'})),
    path('planes/crear-con-factura/', crear_plan_con_factura, name='crear_plan_con_factura'),
    path('ServicioTelefonia/factura/pagar_factura/', pagar_factura, name='pagar_factura'),
    path('ServicioEducacion/', include('ServicioEducacion.urls')),
    path('ServicioLuz/', include('ServicioLuz.urls')),
    path('ServicioInternet/', include('ServicioInternet.urls')),
    path('ServicioAgua/', include('api_recibos_agua.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
