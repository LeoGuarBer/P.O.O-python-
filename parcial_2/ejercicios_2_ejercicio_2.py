class Animal:
    def comer(self):
        return f"El animal come"

class Mamifero(Animal):
    def amamantar(self):
        return f"El mamifero amamanta"

class Ave(Animal):
    def volar(self):
        return f"El ave vuela"
    
class Murcielago (Mamifero,Ave):
    def mostrar_habilidades(self):
        return f"El murcielago tiene las cualidades:\n{super().comer()}\n{super().amamantar()}\n{super().volar()}"

murcielago = Murcielago()

print (Murcielago.mro())
print (murcielago.mostrar_habilidades()) 