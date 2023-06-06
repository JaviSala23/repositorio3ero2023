import sqlite3

conBD=sqlite3.connect("practicasCLI/chat/chat.sqlite")
cursor = conBD.cursor()

cursor.execute("CREATE TABLE Usuarios ( nombre VARCHAR(128), password VARCHAR(128), pclave VARCHAR(128) )")
conBD.close()