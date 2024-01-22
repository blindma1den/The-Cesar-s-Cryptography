//Capturamos variables del DOM
const stringToEncryptInput = document.getElementById('stringToEncrypt-input');
const encryptedText = document.getElementById('encrypted-text');
const encryptButton = document.getElementById('encrypt-button');
const cleanButton = document.getElementById('clean-button');
//Creamos un string con las letras y otro con los números
const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const numbers = '1234567890';
//Dividimos con un epacio cada char, lo invertimos, y volvemos a quitar los espacios y guardamos en variables
const reversedAlphabet = alphabet.split('').reverse().join('');
const reversedNumbers = numbers.split('').reverse().join('');

//Funcion que recibe un string y encripta utilizando el cifrado atBash
const atbashEncrypt = (string) => {
  string = string.toUpperCase();
  let transformedMessage = '';
  let index;
  //Capturamos cada caracter ingresado y chequeamos si es numero o si es texto
  //En cada caso capturamos su indice correspondiente en el string, y lo reemplazamos por el inverso
  //Si el caracter es un espacio o es algun simbolo, no se modificará en la encripción
  for (let i = 0; i < string.length; i++) {
    const char = string[i];

    !isNaN(char)
      ? (index = numbers.indexOf(char))
      : (index = alphabet.indexOf(char));

    if (index !== -1) {
      !isNaN(char)
        ? (transformedMessage += reversedNumbers[index])
        : (transformedMessage += reversedAlphabet[index]);
    } else {
      transformedMessage += char;
    }
  }

  return transformedMessage;
};

//Escuchamos el boton de encrypt y ejecutamos la funcion principal.
encryptButton.addEventListener('click', () => {
  encryptedText.textContent = '';
  const stringToEncrypt = stringToEncryptInput.value;
  const encryptedMessage = atbashEncrypt(stringToEncrypt);
  encryptedText.textContent = encryptedMessage;
});
