peso = float(input("Ingrese su peso en kilogramos por favor: "))
altura = float(input("Ingrese su altura en metros por favor: "))


indiceMasaCorporal = peso / (altura * altura)
print("Su indice de masa corporal es: " + str(indiceMasaCorporal))
