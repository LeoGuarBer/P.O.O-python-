class A:
    def saludar(self):
        return "Hola desde la clase A"
class F:
    def saludar(self):
        return "Hola desde la clase F"
class B(A):
    def saludar(self):
        return "Hola desde la clase B"
class C(F):
    def saludar(self):
        return "Hola desde la clase C"
class D(B,C):
    def saludar(self):
        return "Hola desde la clase D"
    
print(D.mro())