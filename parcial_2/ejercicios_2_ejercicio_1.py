class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"
        
class Estudiante (Persona):
    def __init__(self,nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def mostrar_grado(self):
        return f"Grado: {self.grado}"

job = Estudiante("Job", 18, "3ro")
print(f"Datos crudos: {job.nombre}, {job.edad}, {job.grado}")

print (job.mostrar_datos())
print (job.mostrar_grado())