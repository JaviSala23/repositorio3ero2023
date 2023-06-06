from lib.usuario import Usuario
import getpass

usuario=Usuario()

print(chr(27)+"[0;30m")
print('**************************************************************************************')
print(chr(27)+"[1;31m")
print(chr(27)+"[4;31m"+'\n Bienvenidos al nuevo chat de CLI de ISBH anexo Cruz Alta \n')
print(chr(27)+"[0;30m")
print('**************************************************************************************')

while True:
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
            print('Ingreso a mi sala de chat')
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
        usuario.recuperarContra()
        palabra=input('Palabra clave: ')
    elif opcion==5:
        print('Gracias por usar el chat. que tenga un buen dia.')
        quit()    
    else: 
        print('No existe esa opcion.')