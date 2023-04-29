from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from post.models import Cliente, RegistroLlamadas, Plan, Factura
from post.api.serializers import PostSerilizer,ClienteSerializer ,RegistroLlamadasSerializer,PlanSerializer, FacturaSerializer
from datetime import date


class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerilizer
    queryset = Cliente.objects.all()

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


    @action(detail=True, methods=['put'])
    def cancelar_servicio(self, request, pk=None):
        cliente = self.get_object()
        cliente.servicio_activo = False
        cliente.save()
        serializer = self.serializer_class(cliente)
        return Response({'status': 'OK', 'message': 'Servicio cancelado correctamente.'})

    def update(self, request, pk=None):
        cliente = self.get_object()
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class RegistroLlamadasViewSet(ModelViewSet):
    queryset = RegistroLlamadas.objects.all()
    serializer_class = RegistroLlamadasSerializer

class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)

    #         # Obtener el id del cliente a partir de la solicitud
    #         cliente_id = request.data.get('cliente')

    #         # Obtener el id del plan recién creado
    #         plan_id = serializer.instance.id

    #         # Crear una nueva factura
    #         factura_data = {'cliente': cliente_id, 'plan': plan_id}
    #         factura_serializer = FacturaSerializer(data=factura_data)
    #         if factura_serializer.is_valid():
    #             factura_serializer.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        plan = self.get_object()
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def update(self, request, pk=None):
        factura = self.get_object()
        serializer = FacturaSerializer(factura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def destroy(self, request, pk=None):
        factura = self.get_object()
        factura.delete()
        return Response({'status': 'OK', 'message': 'Factura eliminada correctamente.'})


# @api_view(['POST'])
# def crear_plan_con_factura(request):
#         cliente_id = request.data.get('cliente_id')
#         if not cliente_id:
#             return Response({'error': 'Es necesario proporcionar el ID del cliente.'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             cliente = Cliente.objects.get(pk=cliente_id)
#         except Cliente.DoesNotExist:
#             return Response({'error': f'No se pudo encontrar un cliente con el ID {cliente_id}.'}, status=status.HTTP_404_NOT_FOUND)
        
#         fecha = request.data.get('fecha')
#         if not fecha:
#             return Response({'error': 'Es necesario proporcionar la fecha.'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d').date()
#         except ValueError:
#             return Response({'error': 'Formato de fecha inválido.'}, status=status.HTTP_400_BAD_REQUEST)
    

#         serializer = PlanSerializer(data=request.data)
#         if serializer.is_valid():
#             plan = serializer.save()

#             # Generar factura
#             factura = Factura(cliente=cliente, plan=plan, fecha=fecha)
#             factura.save()

#             serializer = FacturaSerializer(factura)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['POST'])
def crear_plan_con_factura(request):
    serializer = PlanSerializer(data=request.data)
    if serializer.is_valid():
        plan = serializer.save()

        # Generar factura
        cliente_id = request.data.get('cliente_id')
        cliente = Cliente.objects.get(pk=cliente_id)
        fecha = date.today()
        monto = plan.costo_mensual

        factura = Factura(cliente=cliente, plan=plan, fecha=fecha, monto=monto)
        factura.save()

        serializer = FacturaSerializer(factura)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
