from marcas.marcaBase import MarcaBase


class MarcaTesla(MarcaBase):
    def agregados(self):
        return (self.vehiculo._precioBase * 0.5) + 50

    def entregaVehiculo(self):
        modelo = self.vehiculo._modelo
        if modelo == "camioneta":
            nombre = "Cybertruck"
        elif modelo == "carro":
            nombre = "Tesla S"
        elif modelo == "van":
            nombre = "Tesla XL"
        else:
            nombre = "Desconocido"

        print(f"Se ha entregado el vehiculo {nombre} Tesla")
        print(f"Modelo: {self.vehiculo._modelo}, Color: {self.vehiculo._color}")
        print(f"Costo de agregados por la marca: {self.agregados()}")