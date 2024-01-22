##Cifrado Atbash
Atbash es un método de cifrado muy común del alfabeto hebreo. Es parte de la criptografía clásica y es un tipo de **cifrado por sustitución simple monoalfabético**, al igual que Cesar o  ROT-13, entre otros. Se los considera dentro de esa rama, ya que en todos estos métodos de cifrado, se sustituye cada caracter por otro carácter del alfabeto.

En Atbash se utiliza algo tambien conocido como método de espejo, donde se sustituye la primer letra del alfabeto, por la última. **Por ejemplo: A = Z, o B = Y.**

Elegí este tipo de cifrado sabiendo que no es para nada efectivo en la actualidad, ya que es muy fácil de descifrar. Pero me pareció simple de aplicar para el caso en cuestión, y además le integré los números con el mismo proceso para que sea un poco mas completo.
Lo importante es que pude darme cuenta de varias cosas:

**1**- Al ser un proceso de espejo, no es necesario tener un proceso de encriptación y decriptacion, ya que es simétrica la sustitución de las letras. En cambio en Cesar, si le sumas 3 posiciones para encriptar, luego debes restar 3 para desencriptar.

**2**- Teniendo como base al alfabeto, uno puede variar el orden de las letras, y así generar otro tipo de complicación. Por ejemplo ponerle el orden de un teclado QWERTY, donde la Q sería la M, o donde la W sería la N.
A su vez, se puede mezclar esto con el estilo de cifrado de CESAR, y hacer que además de invertir el alfabeto, se resten algunas posiciones. Por ejemplo: Si en  Cesar: A = D  y en Atbash: A = Z. Si yo utilizo primero atbash para llevarla A a Z, y luego le resto tres posiciones a la Z, me quedaría A = W y de esa forma tal vez podría acomplejarse un poco mas el cifrado.