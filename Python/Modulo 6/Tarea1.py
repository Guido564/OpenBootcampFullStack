class Vehiculo:
    color = None
    ruedas = None
    puertas = None
    
class Coche(Vehiculo):
    velocidad = 180
    cilindrada = 1600

c = Coche()

c.color = "Azul"
c.ruedas = 4
c.puertas = 2
print(c.color)
print(c.ruedas)
print(c.puertas)