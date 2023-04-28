from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api_recibos_agua import scraping



@csrf_exempt

def get_deuda(request):
    if request.method == 'POST':
        codigo_cliente = request.POST.get('codigo_cliente')
        correo = "apiagua@gmail.com"
        dni = "87654321"
        url = "https://pagovisa.epstacna.com.pe:8443" 

        deuda = scraping.obtener_deuda(url, codigo_cliente, correo, dni)

        if deuda is not None:
            return JsonResponse({"deuda": deuda})
        else:
            return JsonResponse({"error": "No se encontró información de deuda para el cliente."})
    else:
        return JsonResponse({"error": "Método no permitido."})
