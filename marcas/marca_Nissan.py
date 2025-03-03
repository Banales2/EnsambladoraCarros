from marcas.marcaBase import MarcaBase


class MarcaNissan(MarcaBase):
    def agregados(self):
        return self.vehiculo._precioBase * 0.5

    def entregaVehiculo(self):
        modelo = self.vehiculo._modelo
        if modelo == "camioneta":
            nombre = "Colorado"
        elif modelo == "carro":
            nombre = "Versa"
        elif modelo == "van":
            nombre = "Combi"
        else:
            nombre = "Desconocido"

        print(f"Se ha entregado el vehiculo {nombre} Nissan")
        print(f"Modelo: {self.vehiculo._modelo}, Color: {self.vehiculo._color}")
        print(f"Costo de agregados por la marca: {self.agregados()}")