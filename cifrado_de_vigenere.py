#Definiendo el alfabeto 
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#Función para encriptar 
def encriptar(mensaje, clave):
    mensaje_encriptado = ""

    i = 0

    for letra in mensaje:
        if letra in alfabeto:
            #Calculando el desplazamiento de acuerdo a la clave   
            desplazamiento = ord(clave[i % len(clave)]) - ord('a')
            #Encriptando la letra actual y añadiéndola al mensaje encriptado
            letra_encriptada =chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
            mensaje_encriptado = mensaje_encriptado + letra_encriptada
        else:
            #Si la letra no está en el alfabeto, se la añade tal cual en el mensaje encriptado
            mensaje_encriptado = mensaje_encriptado + letra
        i = (i + 1) % len(clave)

    return mensaje_encriptado


#Función para desencriptar
def desencriptar(mensaje, clave):
    mensaje_desencriptado = ""

    i = 0

    for letra in mensaje:
        if letra in alfabeto:
            #Claculando el desplazamiento de acuerdo a la clave
            desplazamiento = ord(clave[i % len(clave)]) - ord('a')
            #Desencriptando la letra actual y añadiéndola al mensaje desencriptado
            letra_desencriptada =chr((ord(letra) - ord('a') - desplazamiento) % 26 + ord('a'))
            mensaje_desencriptado = mensaje_desencriptado + letra_desencriptada
     
        else:
            #Si la letra no esta en el alfabeto, se la añade asi tal cual
            mensaje_desencriptado = mensaje_desencriptado + letra
        i = (i + 1) % len(clave)

    return mensaje_desencriptado    

#Opciones con las funciones de encriptar y desencriptar
options = {
    "encriptar": encriptar,
    "desencriptar": desencriptar
}      

#Solicitar al ususario que escoja una opción
option = input("Hola, qué desea realizar(encriptar/desencriptar):")

#Verificar si la opción elegida es válida
if option in options:
    #Solicitar al usuario el mensaje y clave 
    mensaje = input("Ingresa el mensaje:")
    clave = input("Ingresa la clave:")

    #Aplicar la función seleccionada por el usuario
    mensaje_final = options[option](mensaje, clave)

    #Mostrar el mensaje original y el mensaje final
    print("Mensaje:" + mensaje)
    print("Mensaje final:" + mensaje_final)
else: 
    #Mensaje de error si la opción ingresada no es válida
    print("Opción no válida")