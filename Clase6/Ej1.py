class Vehiculo():
    color = None
    ruedas = None
    puertas = None
    
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
    
class Coche(Vehiculo):
    velocidad = None
    cilindrara = None
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindradas):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas
        
    def __str__(self) -> str:
        return (f"Caracteristicas del coche:\nColor: {self.color}\nRuedas: {self.ruedas}\nPuertas: {self.puertas}\nVelocidad: {self.velocidad}km/h\nCilindradas: {self.cilindradas}cc")
  
        

coche1 = Coche("rojo", 4, 4, 100, 220)
print(coche1)    
