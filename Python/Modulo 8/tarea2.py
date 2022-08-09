import pickle

class Vehiculo:
    puertas: 0
    marca: None
    
    def __init__(self, puertas, marca):
        self.puertas = puertas
        self.marca = marca
        
    def getMarca(self):
        return self.marca
    
moto = Vehiculo(0, "Honda")
print(moto.getMarca())



f = open("miObjeto.bin", "wb")
pickle.dump(moto, f)
f.close()

f = open("miObjeto.bin", "rb")
honda = pickle.load(f)
f.close()

print(type(honda))
print(moto.getMarca(), "puertas:", moto.puertas)