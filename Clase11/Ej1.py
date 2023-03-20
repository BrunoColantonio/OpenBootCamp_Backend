import sqlite3

connection = sqlite3.connect('Ej1.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Bruno', 'Colantonio')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Martina', 'Diaz')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Nico', 'Rojo')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Lautaro', 'Martinez')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Lionel', 'Messi')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Paulo', 'Dybala')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Lionel', 'Maradona')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Enzo', 'Fernandez')")

connection.commit()


cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Lionel'")


data = cursor.fetchall()
print(data)
connection.close()