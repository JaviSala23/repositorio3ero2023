import sqlite3
from lib.conexion import *

class Usuario:
    def __init__(self): 
        self.nombre=''
        self.contra=''
        self.palabra=''
        
    def registro(self):
        argumento="INSERT INTO Usuarios VALUES ('"+self.nombre+"' ,'"+self.contra+"', '"+self.palabra+"' )"
        base=BaseDatos()
        base.actualizarBD(argumento)
 

    
    def identificarse(self):
        base=BaseDatos()
        argumento="SELECT * FROM Usuarios WHERE nombre='"+self.nombre+"' AND password ='"+self.contra+"'"
        fila=base.consultar(argumento,1)
        return fila
    
    def verUsuarios(self):
        base=BaseDatos()
        argumento="SELECT nombre FROM Usuarios"
        fila=base.consultar(argumento)
        return fila
    
    def recuperarContra():
        pass
    
    def crearCanal():
        pass
    
    def unirCanal():
        pass
    
    def cambiarColor():
        pass
    
    def enviarMensaje():
        pass
        
    def recibirMensaje():
        pass
    