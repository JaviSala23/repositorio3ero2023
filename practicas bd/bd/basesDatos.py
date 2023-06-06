import sqlite3

conBD = sqlite3.connect("practicasCLI/chat/gestion.sqlite")
cursor = conBD.cursor()
#cursor.execute("CREATE TABLE clientes (nombre TEXT, apellido TEXT, dni INTEGER, direccion TEXT)")

nombre = input('escriba su nombre: ')
apellido= input('escriba su apellido: ')
dni= input('escriba su dni: ')
direccion=  input('escriba su direccion: ')

cursor.execute("INSERT INTO clientes VALUES ('"+nombre+"' ,'"+apellido+"', "+dni+", '"+direccion+"')")

conBD.commit()

