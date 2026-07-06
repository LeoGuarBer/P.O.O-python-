class Auto():
    def __init__(self):
        self.estado_del_auto = "apagado"
        
    def encender_auto(self):
        self.estado_del_auto = "encendido"
    
    def conducir_auto(self):
        if self.estado_del_auto == "apagado":
            self.encender_auto()
        print ("Conduciendo el auto")
        
        
bmw_m3 = Auto()
bmw_m3.conducir_auto()