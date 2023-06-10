import datetime
from decimal import Decimal
from rest_framework import status
from rest_framework.response import Response
from money import Money
from observers import PatterObserverPagos, RabbitObserver
from Strategy import DiscountPaymentStrategy, InterestPaymentStrategy


class IServicio:
    def pagar():
        pass
        
class ServicioInternet(IServicio):
    def __init__(pago):
        _pago=pago
        
    def pagar(self, deud_inter):
        observerPago = PatterObserverPagos()
        RabbitObserver = RabbitObserver()

        observerPago.attach_observer(RabbitObserver)
        
        strategy = DiscountPaymentStrategy()
        
        if datetime.date.today() > deud_inter.FechaVencimiento:
            strategy = InterestPaymentStrategy()

        deud_inter_pago = strategy.calculate_payment(deud_inter.MonDeuda,deud_inter.FechaVencimiento )

        deud_inter.MonDeuda = Decimal(deud_inter_pago) - Decimal(self._pago)
        
        if(deud_inter.MonDeuda!=0):
            return {'mensaje': 'El Pago no es el debido', 'status': 400}

        observerPago.notify_observers("Pago Realizado","ServicioInternet")

        deud_inter.save()
        
        if datetime.date.today() > deud_inter.FechaVencimiento:
            return {'mensaje': f'Pago Realizado, con Interes de 20% siendo un total de: {deud_inter_pago}', 'status': 200}
        else:
            return {'mensaje': 'Pago Realizado Total', 'status': 200}
            
        
            

        
        
        
        
    
class ServicioEducacion(IServicio):
    def __init__(pago):
        _pago=pago
    def pagar(self, deuda, cuenta):
        if deuda.Estado:
            return Response({'mensaje': 'La deuda ya ha sido pagada.'}, status=status.HTTP_400_BAD_REQUEST)

        monto_deuda = Decimal(deuda.CantidadDeuda)

        if self._pago != monto_deuda:
            return Response({'mensaje': 'El monto de pago no coincide con la cantidad de deuda.'}, status=status.HTTP_400_BAD_REQUEST)

        divisa_cuenta = cuenta.Divisa

        monto_pago_money = Money(self._pago, "PEN")
        monto_pago_convertido = monto_pago_money.convert(divisa_cuenta)

        if monto_pago_convertido.amount > cuenta.Monto:
            return Response({'mensaje': 'No hay montos suficientes en la cuenta.'}, status=status.HTTP_400_BAD_REQUEST)

        # Seleccionar la estrategia de cálculo de pago según la fecha de vencimiento
        strategy = DiscountPaymentStrategy()
        if datetime.date.today() > deuda.FechaVencimiento:
            strategy = InterestPaymentStrategy()

        monto_pago_final = strategy.calculate_payment(monto_pago_convertido.amount, deuda.FechaVencimiento)

        # Aplicar el descuento a la cuenta
        cuenta.Monto = cuenta.Monto - monto_pago_final
        cuenta.save()

        deuda.Estado = True
        deuda.save()

        observerPagos = PatterObserverPagos()
        
        observer = RabbitObserver()
        observerPagos.attach_observer(observer)
        observerPagos.notify_observers('Pago realizado exitosamente. Monto final: {}'.format(monto_pago_final),"ServicioEducacion")
        return Response({'mensaje': 'Pago realizado exitosamente. Monto final: {}'.format(monto_pago_final)}, status=status.HTTP_200_OK)

        
    
    
class DeudInterPagoFactory:
    @staticmethod
    def create(nameservicio,pagar):
        if (nameservicio=="ServicioInternet"):
            return ServicioInternet(pagar)
    
        if (nameservicio=="ServicioEducacion"):
            return ServicioEducacion(pagar)
            
        
        
        
            
        
        
