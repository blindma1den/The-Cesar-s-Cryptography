def xor_cifrado(texto, clave):
    texto_cifrado = ""
    clave_repetida = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]
    for i in range(len(texto)):
        char = texto[i]
        clave_char = clave_repetida[i]
        xor_result = ord(char) ^ ord(clave_char)
        texto_cifrado += chr(xor_result)
    return texto_cifrado

def xor_descifrado(texto_cifrado, clave):
    texto_descifrado = ""
    clave_repetida = clave * (len(texto_cifrado) // len(clave)) + clave[:len(texto_cifrado) % len(clave)]
    for i in range(len(texto_cifrado)):
        cifrado_char = texto_cifrado[i]
        clave_char = clave_repetida[i]
        descifrado = ord(cifrado_char) ^ ord(clave_char)
        texto_descifrado += chr(descifrado)
    return texto_descifrado

# Ejemplo de uso
texto_original = input("Ingrese el texto a cifrar: ").upper()
clave_secreta = input("Ingrese la clave secreta: ").lower()

texto_cifrado = xor_cifrado(texto_original, clave_secreta)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = xor_descifrado(texto_cifrado, clave_secreta)
print("Texto descifrado:", texto_descifrado)