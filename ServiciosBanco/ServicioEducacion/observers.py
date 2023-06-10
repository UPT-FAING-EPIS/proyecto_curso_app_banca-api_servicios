class ObserverMixin:
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class ConcreteObserver:
    def update(self, instance):
        print("Se ha pagado correctamente")