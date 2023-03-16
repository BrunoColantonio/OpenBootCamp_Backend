import time

#Obtengo la hora
tiempo = time.ctime().split(" ")
tiempo = tiempo[3].split(":")
hora = int(tiempo[0])
minutos = int(tiempo[1])

if hora >= 19:
    print("Ya es hora de irse a casa!")
else:
    print(f"Faltan {19-hora-1}:{60-minutos}hs para irse a casa")
    
