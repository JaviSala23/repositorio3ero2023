#!/usr/bin/env python3
"""Servidor para multitareas"""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


#funcion que permite mas de una coneccion

def accept_incoming_connections():
    """Configurar el manejo de las conecciones"""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

#manejo de clientes
def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        msg_c=msg.decode()
        if msg != bytes("{quit}"):
                broadcast(msg, name+": ")
            
                if msg_c == "Barrera 1":
                        print("barrera1")
                        with open('config.json') as file:
                                data=json.load(file)
                                file.close()
                        data['Barrera']= "1"
                        file= open("config.json", "w+")
                        file.write(json.dumps(data))
                        file.close()
                        
                if msg_c == "Barrera 2":
                        with open('config.json') as file:
                                data=json.load(file)
                                file.close()
                        data['Barrera']= "2"
                        file= open("config.json", "w+")
                        file.write(json.dumps(data))
                        file.close()
                
                if msg_c == "Barrera 3":
                        with open('config.json') as file:
                                data=json.load(file)
                                file.close()
                        data['Barrera']= "3"
                        file= open("config.json", "w+")
                        file.write(json.dumps(data))
                        file.close()


                if msg_c == "C1C":
                        print("Yes")
                        with open('cintas.json') as file:
                                data2=json.load(file)
                                file.close()
                        data2['Cintas']= "0"
                        file= open("cintas.json", "w+")
                        file.write(json.dumps(data2))
                        file.close()
                        #motores(0) 
                if msg_c == "C1D":
                        with open('cintas.json') as file:
                                data2=json.load(file)
                                file.close()
                        data2['Cintas']= "1"
                        file= open("cintas.json", "w+")
                        file.write(json.dumps(data2))
                        file.close()
                        #motores(1)
                if msg_c == "C1OFF":
                        with open('cintas.json') as file:
                                data2=json.load(file)
                                file.close()
                        data2['Cintas']= "2"
                        file= open("cintas.json", "w+")
                        file.write(json.dumps(data2))
                        file.close()
                        #motores(2)
                if msg_c == "C2C":
                        with open('cintas.json') as file:
                                data2=json.load(file)
                                file.close()
                        data2['Cintas']= "3"
                        file= open("cintas.json", "w+")
                        file.write(json.dumps(data2))
                        file.close()
                        #motores(3)
                if msg_c == "C2D":
                        with open('cintas.json') as file:
                                data2=json.load(file)
                                file.close()
                        data2['Cintas']= "4"
                        file= open("cintas.json", "w+")
                        file.write(json.dumps(data2))
                        file.close()
                        #motores(4)
                if msg_c == "C2OFF":
                        with open('cintas.json') as file:
                                data2=json.load(file)
                                file.close()
                        data2['Cintas']= "5"
                        file= open("cintas.json", "w+")
                        file.write(json.dumps(data2))
                        file.close()
                        #motores(5)
#Comandos Ventiladores
                if msg_c == "s1e":
                        print("Silo 1 Encendido")
                        with open('configTemp.json') as file:
                                data4=json.load(file)
                                file.close()
                        data4['Temperatura']= "0"
                        file= open("configTemp.json", "w+")
                        file.write(json.dumps(data4))
                        file.close()
                if msg_c == "s1ap":
                        print("Silo 1 Apagado")
                        with open('configTemp.json') as file:
                                data4=json.load(file)
                                file.close()
                        data4['Temperatura']= "1"
                        file= open("configTemp.json", "w+")
                        file.write(json.dumps(data4))
                        file.close()
                if msg_c == "s2e":
                        print("Silo 2 Encendido")
                        with open('configTemp.json') as file:
                                data4=json.load(file)
                                file.close()
                        data4['Temperatura']= "2"
                        file= open("configTemp.json", "w+")
                        file.write(json.dumps(data4))
                        file.close()
                if msg_c == "s2ap":
                        print("Silo 2 Apagado")
                        with open('configTemp.json') as file:
                                data4=json.load(file)
                                file.close()
                        data4['Temperatura']= "3"
                        file= open("configTemp.json", "w+")
                        file.write(json.dumps(data4))
                        file.close()
                if msg_c == "venAuto":
                        print("Ventiladores Automaticos")
                        with open('configTemp.json') as file:
                                data4=json.load(file)
                                file.close()
                        data4['Temperatura']= "4"
                        file= open("configTemp.json", "w+")
                        file.write(json.dumps(data4))
                        file.close()
                           #CREAR ARCHIVO JSON
                if msg_c == "S1ON":
                        with open('iluminacion.json') as file:
                                data3=json.load(file)
                                file.close()
                        data3['Luces']= "1"
                        file= open("iluminacion.json", "w+")
                        file.write(json.dumps(data3))
                        file.close()

                if msg_c == "S1OFF":
                        with open('iluminacion.json') as file:
                                data3=json.load(file)
                                file.close()
                        data3['Luces']= "2"
                        file= open("iluminacion.json", "w+")
                        file.write(json.dumps(data3))
                        file.close()

                if msg_c == "S2ON":
                        with open('iluminacion.json') as file:
                                data3=json.load(file)
                                file.close()
                        data3['Luces']= "3"
                        file= open("iluminacion.json", "w+")
                        file.write(json.dumps(data3))
                        file.close()

                if msg_c == "S2OFF":
                        with open('iluminacion.json') as file:
                                data3=json.load(file)
                                file.close()
                        data3['Luces']= "4"
                        file= open("iluminacion.json", "w+")
                        file.write(json.dumps(data3))
                        file.close()
        else:
            client.send(bytes("{quit}"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name))
            break

 #envia a todos los conectados el mensaje
def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix)+msg)

        
clients = {}
addresses = {}

HOST = '172.16.254.13'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()