from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import CuentDeudInter
from .serializers import DeudInterSerializer, DeudInterSerializer2
from datetime import datetime
from decimal import Decimal


# Observer patter with singleton

class PatterObserverPagos:
    _instance = None
    _observers = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def attach_observer(self, observer):
        self._observers.append(observer)

    def detach_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

#  y segregacion de interfaces


class Observer:
    def update(self, message):
        pass


class LogObserver(Observer):
    def update(self, message):
        print(f"se ha registrado en el log: {message}")


class EmailObserver(Observer):
    def update(self, message):
        print(f"se envio un Email con: {message}")

# decorator


class IDeudaInterPago:
    def Pagar(self) -> float:
        pass


class DeudaInterPago(IDeudaInterPago):

    def __init__(self, pagar):
        self._pago = float(pagar)

    def Pagar(self) -> float:
        return float(self._pago)


class DeudInterPagoViewDecorator(IDeudaInterPago):
    _component: IDeudaInterPago = None

    def __init__(self, component: IDeudaInterPago) -> None:
        self._component = component

    @property
    def component(self) -> IDeudaInterPago:
        return self._component

    def Pagar(self) -> float:
        return self._component.Pagar()


class DeudaInterPagoMora1(DeudInterPagoViewDecorator):

    def Pagar(self) -> float:
        return self._component.Pagar() - 50


class DeudaInterPagoMora2(DeudInterPagoViewDecorator):

    def Pagar(self) -> float:
        return self._component.Pagar() - 100


class DeudInterListView(viewsets.ModelViewSet):
    serializer_class = DeudInterSerializer
    queryset = CuentDeudInter.objects.all()


# Factory Method pattern

class DeudInterPagoFactory:
    @staticmethod
    def create_deud_inter_pago(rangodemora, pago):
        if rangodemora < 3:
            return DeudaInterPago(pago)
        elif rangodemora < 8:
            return DeudaInterPagoMora1(DeudaInterPago(pago))
        else:
            return DeudaInterPagoMora2(DeudaInterPagoMora1(DeudaInterPago(pago)))


# pattern comando
class Command:
    def execute(self):
        pass


class PagoCommand(Command):
    def __init__(self, deud_inter, pago):
        self.deud_inter = deud_inter
        self.pago = pago

    def execute(self):
        observerPago = PatterObserverPagos()
        observerlog = LogObserver()
        observeremail = EmailObserver()

        observerPago.attach_observer(observerlog)
        observerPago.attach_observer(observeremail)

        diferencia = datetime.date(datetime.now()) - self.deud_inter.FechVenc    # Calcula la diferencia de fechas
        diferencia_en_dias = diferencia.days  # Obtiene la diferencia en días

        deud_inter_pago = DeudInterPagoFactory.create_deud_inter_pago(diferencia_en_dias, Decimal(self.pago))

        self.deud_inter.MonDeuda = Decimal(self.deud_inter.MonDeuda) - Decimal(deud_inter_pago.Pagar())

        if (float(deud_inter_pago.Pagar()) >= self.deud_inter.MonDeuda) or (float(deud_inter_pago.Pagar()) <= 0):
            return {'mensaje': 'El Pago no es el debido', 'status': 400}

        observerPago.notify_observers("el pago se ha realizado")

        self.deud_inter.save()

        if diferencia_en_dias>3:
            return {'mensaje': f'Pago Realizado con extra de mora por lo que solo pagó {deud_inter_pago.Pagar()}', 'status': 200}
        else:
            return {'mensaje': 'Pago Realizado', 'status': 200}


class DeudInterPagoView(generics.RetrieveUpdateAPIView):
    queryset = CuentDeudInter.objects.all()
    serializer_class = DeudInterSerializer2

    lookup_field = 'CodigoDeudInter'
    http_method_names = ['get', 'patch']

    def patch(self, request, *args, **kwargs):
        pago = Decimal(request.data.get('MonPago'))

        if not pago:
            return Response({'error': 'Falta el valor en Monto Pago'}, status=400)

        deud_inter = self.get_object()
        command = PagoCommand(deud_inter, pago)
        result = command.execute()

        if result['status'] == 200:
            serializer = self.get_serializer(deud_inter)
            response_data = {
                'mensaje': result['mensaje'], 'data': serializer.data}
        else:
            response_data = {'mensaje': result['mensaje']}

        return Response(response_data, status=result['status'])
