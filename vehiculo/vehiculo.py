class vehiculo:
    def __init__(self, precioBase, color, modelo):
        self._modelo = modelo
        self._color = color
        self._precioBase = precioBase

    def precioTotal(self, marca):
        tax = marca.agregados()
        return self._precioBase + tax