from ensambladora.Ensambladora import Ensambladora
from vehiculo.vehiculo import vehiculo

vehiculos = [
    vehiculo(100,"Rojo","camioneta"),
    vehiculo(100,"Azul","carro"),
    vehiculo(100,"Verde","van")
]

marca = ["Tesla", "Nissan", "Lamborginni"]

for i in range(len(vehiculos)):
    ensablado = Ensambladora.ensamblado(marca[i], vehiculos[i])
    ensablado.entregaVehiculo()
    print(f"Precio total por el vehiculo {vehiculos[i].precioTotal(ensablado)}")