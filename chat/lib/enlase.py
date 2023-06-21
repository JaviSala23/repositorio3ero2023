import socket
from netifaces import interfaces, ifaddresses, AF_INET
from threading import Thread

class Servidor():
    def __init__(self):
        self.protocolo=(socket.AF_INET, socket.SOCK_STREAM)
        self.anfitrion=""
        self.puerto=""
        self.tamBuffer=1024
        self.enlase=""
        self.nombre=""
        self.direcciones={} #guarda la conexiones del canal
        
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
        while True:
            cliente, direccion_cliente = self.enlase.accept()
            print("%s:%s se ha conectado." % direccion_cliente)
            cliente.send(bytes(f"Bienvendio a el chat: {self.nombre}! "))
            self.direcciones[cliente] = direccion_cliente
            Thread(target=self.manejoCliente, args=(cliente,)).start()
        
    
    def manejoCliente(self,cliente):
        nombre = cliente.recv(self.tamBuffer).decode("utf8")
        msjBienvenda = 'Bienvendio %s! Si quiere salir escriba {quit} .' % nombre
        cliente.send(bytes(msjBienvenda))
        msj = "%s se ha unido al chat!" % nombre
        self.broadcast(bytes(msj))
        self.clientes[cliente] = nombre

        while True:
            msj = cliente.recv(self.tamBuffer)
            
            if msj != bytes("{quit}"):
                    print(nombre+":"+ msj)
                    self.broadcast(msj, nombre+": ")
            else:
                cliente.send(bytes("{quit}"))
                cliente.close()
                del self.clientes[cliente]
                self.broadcast(bytes("%s ha dejado el chat." % nombre))
                break
                
    
    def broadcast(self,msj, prefix=""):
        for sock in self.clientes:
            sock.send(bytes(prefix)+msj)
        
    









class Cliente():
    def __init__(self):
        pass