from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from post.models import Cliente, RegistroLlamadas, Plan, Factura
from post.api.serializers import ClienteSerializer ,RegistroLlamadasSerializer,PlanSerializer, FacturaSerializer
from datetime import date, timedelta


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
#     serializer = PlanSerializer(data=request.data)
#     if serializer.is_valid():
#         plan = serializer.save()

#         # Generar factura
#         cliente_id = request.data.get('cliente_id')
#         cliente = Cliente.objects.get(pk=cliente_id)
#         fecha_emision = date.today()
#         monto = plan.costo_mensual

#         factura = Factura(cliente=cliente, plan=plan, fecha_emision=fecha_emision, monto=monto)
#         factura.save()

#         serializer = FacturaSerializer(factura)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crear_plan_con_factura(request):
    serializer = PlanSerializer(data=request.data)
    if serializer.is_valid():
        plan = serializer.save()

        # Generar factura
        cliente_id = request.data.get('cliente_id')
        cliente = Cliente.objects.get(pk=cliente_id)
        fecha_emision = date.today()
        dias_vencimiento = 30 # Aquí puedes ajustar el número de días que deseas que tenga la factura como vigencia
        fecha_vencimiento = fecha_emision + timedelta(days=dias_vencimiento)
        monto = plan.costo_mensual

        factura = Factura(cliente=cliente, plan=plan, fecha_emision=fecha_emision, fecha_vencimiento=fecha_vencimiento, monto=monto)
        factura.save()

        serializer = FacturaSerializer(factura)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def pagar_factura(request):
    factura = Factura.objects.get(id=request.data['id'])
    factura.pagado = True
    factura.estado = False
    factura.save()
    return Response({'mensaje': 'La factura ha sido pagada.'})