import sqlite3

conBD = sqlite3.connect("practicasCLI/chat/gestion.sqlite")
cursor = conBD.cursor()
datos= cursor.execute("SELECT nombre, apellido FROM clientes")
filas=datos.fetchall()
for fila in filas:
    print(fila)