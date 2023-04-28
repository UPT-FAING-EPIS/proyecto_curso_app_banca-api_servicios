from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from post.models import Cliente, RegistroLlamadas, Plan, Factura
from post.api.serializers import PostSerilizer,ClienteSerializer ,RegistroLlamadasSerializer,PlanSerializer, FacturaSerializer

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