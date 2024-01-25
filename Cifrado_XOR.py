def cifrado_xor(texto, clave):
    resultado = ""
    for i in range(len(texto)):
        resultado += chr(ord(texto[i]) ^ ord(clave[i % len(clave)]))
    return resultado

# Ejemplo de uso
mensaje_original = "Hola, Mundo!"
clave = "clave"

# Cifrado
mensaje_cifrado = cifrado_xor(mensaje_original, clave)
print("Mensaje cifrado:", mensaje_cifrado)

# Descifrado
mensaje_descifrado = cifrado_xor(mensaje_cifrado, clave)
print("Mensaje descifrado:", mensaje_descifrado)
