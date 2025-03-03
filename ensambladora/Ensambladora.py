from marcas.marca_Lamborginni import MarcaLamborginni
from marcas.marca_Nissan import MarcaNissan
from marcas.marca_Tesla import MarcaTesla

class Ensambladora:
    @staticmethod
    def ensamblado(marca, vehiculo):
        if marca == "Tesla":
            return MarcaTesla(vehiculo)
        elif marca == "Nissan":
            return MarcaNissan(vehiculo)
        elif marca == "Lamborginni":
            return MarcaLamborginni(vehiculo)
        else:
            print("Marca Invalida")
