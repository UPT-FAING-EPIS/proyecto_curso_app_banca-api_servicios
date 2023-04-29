from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_recibos_agua/', include('api_recibos_agua.urls')),  # Include the app's URLs
]