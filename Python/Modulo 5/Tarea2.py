def numeroPrimo(numero):
    for i in range(2, numero):
        if (numero % i) == 0:
           print("No es primo")
           break
    else:
        print("Es primo")
        
        
         
numeroPrimo(17)