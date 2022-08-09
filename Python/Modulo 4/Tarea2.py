def numero_impar(numero_inicial, numero_final):
    while numero_inicial < numero_final:
        if(numero_inicial % 2 == 1):
            print(numero_inicial)
        numero_inicial += 1
        
                
print(numero_impar(3, 8))

