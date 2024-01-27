#!/bin/bash

# Función para cifrar un solo carácter
# Se define una funcion CIPER_CHAR que toma dos parámetros: CHAR y KEY_CHAR
cipher_char() {

	#$1 y $2 como argumentos que se le entregan a la funcion.
	#$1 es CHAR y $2 es KEY_CHAR
	#Se declara ALPHABET, una variable que contiene todas las letras del abecedario

    local char="$1"
    local key_char="$2"
    local alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


	#Estructura condicional que verifica si el caracter CHAR es una letra mayuscula
	#Con ayuda del operador =~ para verificar el patron    
    if [[ $char =~ [A-Z] ]]; then


	#char_pos... utiliza la funcion EXPR INDEX para encontrar la posicion de CHAR
	#en ALPHABET y resta 1 para obtener el INDICE
	#Debido a que los indices comienzan desde 0. A=0, B=1...
        char_pos=$(( $(expr index "$alphabet" "$char") - 1 ))


	#key_pos...  Similar al anterior, encuentra la posicion de KEY_CHAR
	#en ALPHABET y resta 1 para obtener el INDICE
        key_pos=$(( $(expr index "$alphabet" "$key_char") - 1 ))

	
	#Calculamos la posicion cifrada usando la formula del cifrado Vigenere
        cipher_pos=$(( (char_pos + key_pos) % 26 ))


	#Extraemos el caracter cifrado de ALPHABET utilizando el INDICE calculado
	#utilizamos ${variable:start:count} para extraer un solo caracter
	#de la -variable- ALPHABET en la posicion -start- que es CIPHER_POS
	#y -count- es 1 pues significa que solo se extrae un solo caracter
        cipher_char="${alphabet:$cipher_pos:1}"

	
	#ECHO -N CIPHER_CHAR es el caracter cifrado de la operacion anterior
	#Y se imprime en la consola sin añadir el salto de linea
        echo -n "$cipher_char"

	#ELSE -sino- en el caso que el caracter no es una letra mayuscula
	#imprimira el caracter original sin cifrar
    else
        echo -n "$char"
    fi
}




# Función para cifrar un mensaje completo
vigenere_cipher() {

	#definimos 2 parametros para la funcion MESSAGE y KEY
	#KEY_LENGHT es la longitud en numero de la KEY o palabra clave

    local message="$1"
    local key="$2"
    local key_length=${#key}


	#Bucle FOR que recorre cada caracter del mensaje de 1 en 1

    for ((i = 0; i < ${#message}; i++)); do

	#char=... Extraemos el caracter actual del mensaje con ayuda de i que es
	#la posicion de FOR, es decir, extraemos el caracter donde esta i en ese 
	#momento
        char="${message:$i:1}"

	#key_char=... Extraemos el caracter actual de la llave con ayuda de i que es
	#la posicion de FOR igualmente, es decir, i en la posicion que sea en la KEY
        key_char="${key:$(($i % key_length)):1}"

	#Llamamos a la funcion cipher_char para cifrar los caracteres actuales
        cipher_char "$char" "$key_char"
    done

	#echo Imprimimos una nueva linea al final del cifrado
    echo
}




# Solicita al usuario que ingrese el mensaje y la palabra clave

	#read Lee la entrada o el ingresar del usuario
	#-p muestra un mensaje en la consola antes de leer lo ingresado
read -p "Ingresa el mensaje a cifrar: " user_message
read -p "Ingresa la palabra clave: " user_key



# Convierte el mensaje y la palabra clave a mayúsculas

	#message_uppercase=... sustituimos comandos entre parentesis y se evalua
	#y se utiliza como valor

	#echo user...Utilizamos TR a-z A-Z para convertir el mensaje ingresado
	#a mayusculas
message_uppercase=$(echo "$user_message" | tr 'a-z' 'A-Z')
key_uppercase=$(echo "$user_key" | tr 'a-z' 'A-Z')



# Cifra el mensaje e imprime el resultado

	#Imprimimos el mensaje cifrado llamando la funcion vigenere cipher
	#con los valores que ingresa el usuario y se muestra el resultado
echo "Mensaje Cifrado: $(vigenere_cipher "$message_uppercase" "$key_uppercase")"
