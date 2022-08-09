def anioBisiesto(anio):
    if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        return False
    else:
        return True
        

print(anioBisiesto(2500))

