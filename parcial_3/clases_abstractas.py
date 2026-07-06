from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.ocupacion = ocupacion
    
    @abstractclassmethod
    def presentar_ocupacion(self):
        pass
    
    def presentarse(self):
        print (f"Hola soy {self.nombre}, y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, ocupacion):
        super().__init__(nombre, edad, sexo, ocupacion)
        
    def presentar_ocupacion(self):
        print (f"Estoy estudiando la carrera de {self.ocupacion}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, ocupacion):
        super().__init__(nombre, edad, sexo, ocupacion)
        
    def presentar_ocupacion(self):
        print (f"Estoy trabajando como {self.ocupacion}")


juanito = Estudiante("Juanito", 18, "Masculino", "Turismo")
don_juan = Trabajador("Don Juan", 58, "Masculino", "Albañil")

juanito.presentarse()
juanito.presentar_ocupacion()

don_juan.presentarse()
don_juan.presentar_ocupacion()