import socket
import sys
#crear una coneccion tipo socket de tcp/ip
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definimos el anfitrion

anfitrion = 'localhost'

# deginimos el puerto

puerto = 8080

# juntar el anfitrion con el puerto.. host, con el port

sock.bind((anfitrion, puerto))

# escucha conexiones entrantes

sock.listen(1)


# Espera por una conexion

print('Esperando la conexion')

conn, cliente = sock.accept()

print(cliente, 'Conectado!')

# Recive un dato y lo retransmite

data = conn.recv(16)

print (str(data))

if data:

    conn.sendall(data)

else:

    print('No hay datos del cliente: ', cliente)

# Close the connection

conn.close()

