from marcas.marcaBase import MarcaBase


class MarcaLamborginni(MarcaBase):
    def agregados(self):
        return self.vehiculo._precioBase * 2

    def entregaVehiculo(self):
        modelo = self.vehiculo._modelo
        if modelo == "camioneta":
            nombre = "Lamborginni Urus"
        elif modelo == "carro":
            nombre = "Lamborghini Diablo."
        elif modelo == "van":
            nombre = "Lamborghini Fatboy"
        else:
            nombre = "Desconocido"

        print(f"Se ha entregado el vehiculo {nombre}")
        print(f"Modelo: {self.vehiculo._modelo}, Color: {self.vehiculo._color}")
        print(f"Costo de agregados por la marca: {self.agregados()}")