class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print (f"El estudiante '{self.nombre}' está estudiando")
        
nombre = input("Ingresa tu nombre:  ")
edad = input("Ingresa tu edad:  ")
grado = input("Que semestre estas cursando:  ")

estudiante = Estudiante(nombre,edad,grado)

clave = input("Ingresa la clave:  ")

if clave.lower() == "estudiar":
    estudiante.estudiar()