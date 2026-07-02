from herencia_simple import Persona

class Artista:
    def __init__(self, disciplina):
        self.disciplina = disciplina
        
    def mostrar_habilidades(self):
        return f"Soy un artista especializado en {self.disciplina}"
    
class EmpleadoArtista (Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, disciplina, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, disciplina)
        self.empresa = empresa
        self.salario = salario
    def mostrar_informacion(self):
        return f"Hola soy {self.nombre}, soy de {self.nacionalidad}, tengo {self.edad} años de edad, {super().mostrar_habilidades()}, trabajo en {self.empresa} y gano {self.salario} pesos al mes"

nuggets = EmpleadoArtista("Luis", 18, "Mexico", "Musica", "Bar 27", 20000)

print (nuggets.mostrar_informacion())

herencia = issubclass(EmpleadoArtista, Persona)
instancia = isinstance(nuggets, Persona)

print (herencia)
print (instancia)