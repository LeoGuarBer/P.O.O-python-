class Celular:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
celular_1 = Celular("Apple" , "iPhone 15", "Negro")
print(celular_1.modelo)