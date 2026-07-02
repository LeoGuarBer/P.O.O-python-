class ClasePrivada:
    def __init__(self,usuario,contraseña):
        self._usuario = usuario
        self.__contraseña = contraseña
        
        
cuenta = ClasePrivada("Leoguez","Cars.1234")

print(cuenta._usuario)