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
        del base #elimina el objeto creado
 

    
    def identificarse(self):
        base=BaseDatos()
        argumento="SELECT * FROM Usuarios WHERE nombre='"+self.nombre+"' AND password ='"+self.contra+"'"
        fila=base.consultar(argumento,1)
        del base
        return fila
    
    def verUsuarios(self):
        base=BaseDatos()
        argumento="SELECT nombre FROM Usuarios"
        fila=base.consultar(argumento)
        del base
        return fila
    
    def consultarPalabraClave(self):
        base=BaseDatos()
        argumento="SELECT * FROM Usuarios WHERE nombre='"+self.nombre+"' AND pclave ='"+self.palabra+"'"
        fila=base.consultar(argumento,1)
        del base
        return fila
    
    def recuperarContra(self):
        base=BaseDatos()
        argumento="UPDATE Usuarios SET password='"+self.contra+"' WHERE nombre='"+self.nombre+"' AND pclave='"+self.palabra+"'"
        base.actualizarBD(argumento)
        del base
        

    