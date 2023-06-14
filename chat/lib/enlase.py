import socket
from netifaces import interfaces, ifaddresses, AF_INET

class Servidor():
    def __init__(self):
        self.protocolo=(socket.AF_INET, socket.SOCK_STREAM)
        self.anfitrion=""
        self.puerto=""
        self.tamBuffer=1024
        self.enlase=""
        self.nombre=""
        
    def crearCanal(self):
        try:
            for ifaceName in interfaces():
                addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
                ip=addresses
            self.anfitrion=ip[0]
            
            self.enlase = socket.socket(self.protocolo[0],self.protocolo[1])
            self.enlase.bind((self.anfitrion, int(self.puerto)))
            return True
        except:
            return False
        
           
    def gestConEntr(self):
        pass
    
    def recibirMen(self):
        pass
    
    def enviarMen(self):
        pass
        
    









class Cliente():
    def __init__(self):
        pass