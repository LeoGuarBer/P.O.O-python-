def decorador(funcion):
    def funcion_modificada(funcion):
        print ("="*10)
        funcion()
        print ("="*10)
    
    return funcion_modificada(funcion)

@decorador
def saludo():
    print ("Hola")
    
# saludo()