import threading
from time import sleep


def primera():
    while True:
        print("Primer hilo corriendo")
        sleep(0.2)
        
def segundo():
    while True:
        print("Segundo hilo corriendo")
        sleep(1)

def tercero():
    while True:
        print("Tercer hilo corriendo")
        sleep(5)

# creamos los hilos
hilo1 = threading.Thread(target=primera,name='hilo1')
hilo2 = threading.Thread(target=segundo,name='hilo2')
hilo3 = threading.Thread(target=tercero,name='hilo3')

# ejecutamos los hilos
hilo1.start()
hilo2.start()
hilo3.start()
