from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api_recibos_agua import views
schema_view = get_schema_view(
   openapi.Info(
      title="API Documentación",
      default_version='v1',
      description="Documentación de la API de servicio de agua",
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_recibos_agua.urls')),
    path('', RedirectView.as_view(url='/admin/'), name='index'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('deuda/', views.get_deuda, name='get_deuda'),
]