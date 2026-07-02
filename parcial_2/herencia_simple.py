class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def presentacion(self):
        return f"Hola soy {self.nombre}, tengo {self.edad} años de edad y soy de {self.nacionalidad}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, grado, universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.grado = grado
        self.universidad = universidad
        
leo = Estudiante("Leo",18,"Mexicana","Ingeniería en Sistemas","UNAM")