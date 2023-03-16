class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
 
    def print(self):
               print("Nombre:", self.nombre)
               print("Nota:", self.nota)
 
    def resultado(self):
            if self.nota >= 4:
                print("El alumno ha aprobado!")
            else:
                print("El alumno ha reprobado")
 
 
 
alumno1 = Alumno()
alumno2 = Alumno()
 
alumno1.inicializar("Martina", 9)
alumno2.inicializar("Marcos", 3)
 
alumno1.print()
alumno1.resultado()
alumno2.print()
alumno2.resultado()