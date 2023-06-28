from lib.usuario import Usuario
from lib.enlase import Servidor,Cliente
import getpass
from threading import Thread



print(chr(27)+"[0;30m")
print('**************************************************************************************')
print(chr(27)+"[1;31m")
print(chr(27)+"[4;31m"+'\n Bienvenidos al nuevo chat de CLI de ISBH anexo Cruz Alta \n')
print(chr(27)+"[0;30m")
print('**************************************************************************************')


def main():
    
    while True:
        usuario=Usuario()
        print(chr(27)+"[0;32m")
        print(chr(27)+"[1;32m")
        opcion=int(input('''
                    Seleccione una opcion:
                    1- Identificarse
                    2- Registrarse
                    3- Traer usuarios existentes
                    4- No recuerdo mi contraseña
                    5- Salir
                    \ṇ̣
                    Opcion: 
                    '''))
        
        
        if opcion==1:
            print(chr(27)+"[0;33m"+ 'Para ingresar al por favor Indentificate:')
            usuario.nombre=input('Nombre de usuario: ')
            usuario.contra=getpass.getpass('Contraseña: ')
            fila=usuario.identificarse()
            if fila:
                print(chr(27)+"[0;30m")
                print('**************************************************************************************')
                print(chr(27)+"[1;31m")
                print(chr(27)+"[4;34m"+'\n Bienvenido '+usuario.nombre +' a lobby del chat \n')
                print(chr(27)+"[0;30m")
                print('**************************************************************************************')
                chat(usuario)
                break
            else: 
                print("Usuario o contraseña invalida")
            
        elif opcion==2:
            print(chr(27)+"[1;33m"+'Bienvendio Usuario Nuevo \n ingrese los siguentes datos')
            usuario.nombre= input('Ingrese un nombre de usuario: ')
            usuario.contra= getpass.getpass('Ingrese una contraseña: ')
            usuario.palabra= input('Ingrese una palabra clave: ')
            usuario.registro()
            
        elif opcion==3:
            usuarios=usuario.verUsuarios()
            print(usuarios)
            
        elif opcion==4:
            usuario.nombre=input('Ingrese un nombre de usuario: ')
            usuario.palabra=input('Ingrese la palabra clave: ')
            fila=usuario.consultarPalabraClave()
            if fila:
                usuario.contra=getpass.getpass("Ingrese su nueva contraseña: ")
                usuario.recuperarContra()
            
        elif opcion==5:
            print('Gracias por usar el chat. que tenga un buen dia.')
            quit()    
        else: 
            print('No existe esa opcion.')
            

def chat(usuario):
    while True:
        print(chr(27)+"[0;32m")
        print(chr(27)+"[1;35m")
        opcion=int(input('''
                    Seleccione una opcion:
                    1-Crear canal
                    2-Ver canales
                    3-Unirse a un canal
                    4-Cerrar sesion
                    5-Salir 
                    \ṇ̣
                    Opcion: 
                    '''))
        
        if opcion==1:
            canal1=Servidor()
            canal1.puerto=input("Ingrese un puerto de servicio desde el 8000 al 8040: ")
            canal1.nombre=input("Ingrese un nombre para su canal: ")
            retorno=canal1.crearCanal()
            
           
            if retorno:
                print("El canal : '"+ canal1.nombre + "' ha sido creado.")
                print("Esperando conexiones...")
                canal1.enlase.listen(5)
                hilo_aceptar = Thread(target=canal1.gestConEntr)
                hilo_aceptar.start()
                hilo_aceptar.join()
                canal1.enlase.close()
                
            else:
                print("No se pudo crear el canal")
            
        
        elif opcion==2:
            print('canales')
        elif opcion==3:
            cliente1=Cliente()
            cliente1.ip=input('Ingrese el IP del canal: ')
            cliente1.puerto=int(input('Ingrese el puerto del canal:'))
            cliente1.conectar()
            hilo_enviar = Thread(target=cliente1.enviarMsj)
            hilo_recibir= Thread(target=cliente1.recibirMsj)
            hilo_enviar.start()
            hilo_recibir.start()
            break
        elif opcion==4:
            del usuario #elimina el objeto creado
            main()
        elif opcion==5:
            print('Gracias por usar el chat. que tenga un buen dia.')
            quit()    
        else:
            print('No existe esa opcion.')
        
         
        
            
            
            
            














            
if __name__ == "__main__":
   main()