from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .decorators import check_post_request
from . import scraping  # Asegúrate de tener este import si estás utilizando la función obtener_deuda desde el módulo scraping

@csrf_exempt
@check_post_request
def get_deuda(request):
    codigo_cliente = request.POST.get('codigo_cliente')
    correo = "apiagua@gmail.com"
    dni = "87654321"
    url = "https://pagovisa.epstacna.com.pe:8443" 

    deuda = scraping.obtener_deuda(url, codigo_cliente, correo, dni)

    if deuda is not None:
        return JsonResponse({"deuda": deuda})
    else:
        return JsonResponse({"error": "No se encontró información de deuda para el cliente."})
