                #FUNCION QUE DETERMINA SI ES BISIESTO O NO
def esBisiesto(anio):
    if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
      return True
    else:
        return False
    
                #MAIN
anio = input("Ingrese el año el cual desea saber si es bisiesto: ")
anio = int(anio)
if(esBisiesto(anio)):
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} NO es bisiesto")
    
    