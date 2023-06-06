import sqlite3

class BaseDatos():
    def __init__(self):
        self.bd="practicasCLI/chat/chat.sqlite" 
        self.conexion=""
        self.cursor=""
        
    def conectar(self):
       self.conexion=sqlite3.connect("practicasCLI/chat/chat.sqlite")
       self.cursor = self.conexion.cursor() 
    
    def actualizarBD(self,argumento):
        self.conectar()
        self.cursor.execute(argumento)
        self.conexion.commit()
        self.conexion.close()
    
    def consultar(self,argumento):
        self.conectar()
        datos=self.cursor.execute(argumento)
        fila=datos.fetchone()
        return fila
        
        
        