class User:
    def __init__ (self, user, password):
        self.user = user
        self.__password = password
        
    def get_password(self):
        return self.__password
    def set_password(self, new_password):
        self.__password = new_password
        
    
user = input("Ingresa el usuario:  ")
password = input ("Ingresa la contraseña:  ")

account = User(user,password)

while True:
    change_password = input("\n¿Quieres cambiar la contraseña? (s/n):  ")
    if change_password == "s":
        new_password = input("Ingresa la nueva contraseña:  ")
        account.set_password(new_password)
        break
    else:
        print("Cambia la contraseña")
        
        
print (account.user)
print (account.get_password())