

from django.http import HttpRequest, JsonResponse
from django.test import TestCase
from api_recibos_agua.decorators import check_post_request
import json

class GetDeudaTest(TestCase):
    def test_post_request(self):
        @check_post_request
        def my_view(request):
            return JsonResponse({"message": "POST request received"})

        request = HttpRequest()
        request.method = 'POST'

        response = my_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"message": "POST request received"})

    def test_non_post_request(self):
        @check_post_request
        def my_view(request):
            return JsonResponse({"message": "This should not happen"})

        request = HttpRequest()
        request.method = 'GET'

        response = my_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"error": "Método no permitido. Solo se aceptan peticiones POST."})
