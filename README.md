

Cifrado Atbash, historia, características y aplicación.

La criptografía se ha convertido en la base de cualquier proceso de seguridad informática y consiste en usar técnicas que permiten alterar y modificar mensajes o archivos con el objetivo de que no puedan ser leídos por todos aquellos usuarios que no estén autorizados para hacerlo. 
Existen múltiples técnicas para hacer criptografía, entre estas destacan: 
Cifrado César; Cifrado Vigénere; Cifrado de sustitución simple; Cifrado de Transposición; Cifrado RSA; Cifrado AES; Cifrado DES; Cifrado Blowfish; Cifrado de curva elíptica; Cifrado de Flujo; Cifrado homomórfico. 
En esta investigación desarrollaré el Cifrado Atbash, un método de cifrado por sustitución simple.
El cifrado Atbash se menciona por primera vez en el libro bíblico de Jeremías, donde se usa para cifrar el nombre de Babel. En este caso, se utilizaba el alfabeto hebreo, donde la primera letra se sustituyó con la última, la segunda con la penúltima, la tercera con la antepenúltima y así sucesivamente, por lo que también se conoce como Cifrado Espejo. 
Cómo en el alfabeto hebreo no existen las vocales, al aplicar el cifrado Atbash al español, es poco probable que las palabras sean fácilmente pronunciables. Sin embargo, al ser un cifrado de sustitución simple, puede ser fácilmente vulnerado. Por esta razón, la usaré solo para fines educativos. 
El cifrado Atbash, un método de sustitución simple, es un tipo de sustitución monoalfabética ya que usa una sustitución fija para todo el mensaje gracias al uso de un alfabeto invertido. 
Bajo este concepto, el Cifrado Atbash funciona de acuerdo con la siguiente guía: 
A=Z | N=M
B=Y | O=L
C=X | P=K
D=W | Q=J
E=V | R=I
F=U | S=H
G=T | T=G
H=S | U=F
I=R | V=E
J=Q | W=D
K=P | X=C
L=O | Y=B
M=N | Z=A
Para realizar el cifrado Atbash, propongo el siguiente código de Python cuyo objetivo es ingresar un texto para ser cifrado utilizando el alfabeto inverso.
La definición de la función <cifrado_atbash> toma el 'texto' como argumento y debemos definir el alfabeto original, el alfabeto inverso o cifrado y se usa el bucle for para iterar sobre cada letra del texto original. Posteriormente se verifica la presencia de las letras en el alfabeto original y su correspondencia en el alfabeto cifrado o inverso yo btenemos el texto cifrado. Debemos tomar en cuenta el uso de mayúsculas y minúsculas para este ejercicio. 
La instrucción es que, por cada letra en el texto original, el programa debe tomar una letra del alfabeto y sustituirla por la letra correspondiente del alfabeto inverso. Una vez realizado el proceso, tendremos el texto cifrado.
 
Referencias 
1. Profe Sang (diciembre 2022, enero 2023). Curso de criptografía. Publicado en https://www.youtube.com/@ProfeSang
2. Nic Argentina (marzo 2018). ¿Qué es criptografía?. Publicado en https://nic.ar/es/enterate/novedades/que-es-criptografia#:~:text=La%20criptograf%C3%ADa%20es%20el%20desarrollo,no%20est%C3%A9n%20 autorizados a hacerlo.
3. Universidad de Granada (SF). El método Atbash. Publicado en https://www.ugr.es/~anillos/textos/pdf/2010/EXPO-1.Criptografia/02a01.htm
4. Wikipedia (SF). Cifrado por sustitución. Publicado en https://es.wikipedia.org/wiki/Cifrado_por_sustituci%C3%B3n 
5. Wikipedia (SF). Atbash. Publicado en https://es.wikipedia.org/wiki/Atbash 
6. OpenAI (2023). `cifrado_atbash´. 
 
