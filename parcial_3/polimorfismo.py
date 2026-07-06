class Perro:
    def sonido(self):
        return "Guau"
    
class Gato:
    def sonido(self):
        return "Miaw"
    
def hacer_sonido(animal):
    print (animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(gato)
hacer_sonido(perro)