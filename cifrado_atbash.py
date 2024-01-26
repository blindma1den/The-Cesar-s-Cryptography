

def cifrado_atbash(texto):
    alfabeto_original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabeto_cifrado = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    texto_cifrado = ''

    for letra in texto:
        if letra.upper() in alfabeto_original:
            indice_original = alfabeto_original.index(letra.upper())
            letra_cifrada = alfabeto_cifrado[indice_original]
            if letra.islower():
                letra_cifrada = letra_cifrada.lower()
            texto_cifrado += letra_cifrada
        else:
            texto_cifrado += letra

    return texto_cifrado

# Solicitar al usuario que ingrese un texto
texto_original = input("Ingrese el texto a cifrar: ")

# Llamar a la función cifrado_atbash y mostrar el resultado
texto_cifrado = cifrado_atbash(texto_original)
print(f"Texto cifrado: {texto_cifrado}")

