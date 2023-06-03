from functools import wraps
from django.http import JsonResponse

def check_post_request(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != 'POST':
            return JsonResponse({"error": "Método no permitido. Solo se aceptan peticiones POST."})
        return view_func(request, *args, **kwargs)
    return _wrapped_view
