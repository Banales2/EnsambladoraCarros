from abc import ABC, abstractmethod

class MarcaBase(ABC):
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo

    @abstractmethod
    def agregados(self):
        pass

    @abstractmethod
    def entregaVehiculo(self):
        pass