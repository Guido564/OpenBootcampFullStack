from functools import reduce

numeros = input("ingrese numeros:")
numerosEnList = sorted(numeros)
print(numerosEnList)
numerosImpares = []

for i in numerosEnList:
    if int(i) % 2 != 0:
        numerosImpares.append(int(i))
        
print(numerosImpares)

def suma(a, b):
    return a + b

resultado = reduce(suma, numerosImpares)

print(resultado)

