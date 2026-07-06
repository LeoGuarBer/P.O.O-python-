class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"[La persona se llama {self.nombre}, Su edad es de {self.edad} años]"
    
    def __repr__(self):
        return f"Persona('{self.nombre}',{self.edad})"
    
    def __add__(self, other):
        edad_sumada = self.edad + other.edad
        descendencia = self.nombre + " y es hijo de " + other.nombre
        return Persona(descendencia,edad_sumada)
    
pedro = Persona("Pedro",12)

print(pedro)
# representacion = repr(pedro)
# resultado = representacion.replace("Pedro Leon Garza Jaramillo","Pedro")
# resultado = resultado.replace("21","20")
# Pedro_simplificado = eval(resultado)
# print (Pedro_simplificado)

juan = Persona ("Juan", 30)

suma = pedro + juan

print (suma)