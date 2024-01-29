**HISTORIA**
El cifrado Vigenère es un cifrado polialfabético que originalmente fue descrito por Giovan Battista Belasso en 1553, pero se lo atribuyo de manera errónea a 
Blaise de Vigenère en el siglo XIX. Tuvo una reputación de ser irrompible, sin embargo pudo ser descifrado por el método Kasiski y criptoanalistas. 
Se propusieron variaciones del cifrado Vigenere en el siglo XIX pero a pesar de ello seguía siendo vulnerable. Gilbert Vernam fue uno de los que intentó corregir 
las vulnerabilidades con el cifrado Vernam-Vigenère en 1918, pero el cifrado continua siendo susceptible al criptoanálisis.

**FORMA DE USO**
1. Mensaje a cifrar
2. Elección de una palabra clave
3. La palabra clave debe tener la misma longitud que el mensaje
4. Cifrar cada letra del mensaje sumando los indices de las letras del mensaje y de la clave
5. La suma no debe superar el numero 26, ya que es la cantidad de letras en el alfabeto
6. Finalmente de acuerdo a la suma de indices, se asigna la letra correspondiente del alfabeto
7. Se obtiene el mensaje cifrado
8. Para descifrar el mensaje se realiza el proceso inverso

**INSTRUCCIONES PARA CORRER EL PROGRAMA DESDE UNA MÁQUINA VIRTUAL KALI LINUX**
1.  Abrir la terminal y colocar la ruta del directorio en el que se encuentra el archivo
    cd /rutadeldirectorio
2.  Ejecutar el archivo de la siguiente manera
    python nombre_archivo.py
