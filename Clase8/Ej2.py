from pickle import *
# import pickle

class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        # return self.color + " " + self.ruedas
        return f"color: {self.color}\nruedas: {self.ruedas}"


audi = Vehiculo("rojo", "4")
file = open("./Clase8/file_vehiculo", "w+b")

dump(audi, file)

file.seek(0)
otro_audi = load(file)

print(otro_audi)
file.close()