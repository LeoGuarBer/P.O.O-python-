class User():
    def __init__(self, correo, contraseña):
        self.correo = correo
        self.__contraseña = contraseña
        
    @property
    def contraseña(self):
        return self.__contraseña
    
    @contraseña.setter
    def contraseña(self,contraseña):
        self.__contraseña = contraseña 
    
    @contraseña.deleter
    def contraseña(self):
        del self.__contraseña
        

usuario = User("Luis","1234")

print (usuario.contraseña)

usuario.contraseña = "2349"
print (usuario.contraseña)

del usuario.contraseña