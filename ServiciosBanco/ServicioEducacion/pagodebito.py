import datetime
from decimal import Decimal
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import tbCuenta, tbDeudasAlumno
from .money import Money
from .observers import ConcreteObserver, ObserverMixin
from .paymentstrategy import DiscountPaymentStrategy, InterestPaymentStrategy

class PagoDebitoViews(APIView):
    def post(self, request):
        codigo_deuda = request.data.get('CodigoDeuda')
        codigo_cuenta = request.data.get('CodigoCuenta')
        monto_pago = request.data.get('MontoPago')

        deuda = get_object_or_404(tbDeudasAlumno, CodigoDeuda=codigo_deuda)
        cuenta = get_object_or_404(tbCuenta, CodigoCuenta=codigo_cuenta)

        return self.realizar_pago(deuda, cuenta, monto_pago)

    def realizar_pago(self, deuda, cuenta, monto_pago):
        if deuda.Estado:
            return Response({'mensaje': 'La deuda ya ha sido pagada.'}, status=status.HTTP_400_BAD_REQUEST)

        monto_deuda = Decimal(deuda.CantidadDeuda)

        if monto_pago != monto_deuda:
            return Response({'mensaje': 'El monto de pago no coincide con la cantidad de deuda.'}, status=status.HTTP_400_BAD_REQUEST)

        divisa_cuenta = cuenta.Divisa

        monto_pago_money = Money(monto_pago, "PEN")
        monto_pago_convertido = monto_pago_money.convert(divisa_cuenta)

        if monto_pago_convertido.amount > cuenta.Monto:
            return Response({'mensaje': 'No hay montos suficientes en la cuenta.'}, status=status.HTTP_400_BAD_REQUEST)

        # Seleccionar la estrategia de cálculo de pago según la fecha de vencimiento
        strategy = DiscountPaymentStrategy()
        if datetime.date.today() > deuda.FechaVencimiento:
            strategy = InterestPaymentStrategy()

        monto_pago_final = strategy.calculate_payment(monto_pago_convertido.amount, deuda.FechaVencimiento)

        # Aplicar el descuento a la cuenta
        cuenta.Monto -= monto_pago_final
        cuenta.save()

        deuda.Estado = True
        deuda.save()

        observer = ConcreteObserver()
        deuda.add_observer(observer)
        deuda.notify_observers()  # Notificar observadores de cambio de estado

        return Response({'mensaje': 'Pago realizado exitosamente. Monto final: {}'.format(monto_pago_final)}, status=status.HTTP_200_OK)
