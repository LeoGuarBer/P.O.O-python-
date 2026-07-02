class Celular:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def llamar (self, numero):
        print (f"Llamando desde tu {self.modelo} al: {numero}")
    
celular_1 = Celular("Apple" , "iPhone 15", "Negro")
print(celular_1.modelo)
celular_1.llamar(4495504813)