# Challenge lvl2 - Discord blindma1den
For this challenge I decided to implement a couple of ciphers. Due to work I am still working on it. I finish the first one which is Affine cipher. So for now this will be my submission.

### History of Affine Cipher
The Affine cipher is a cryptographic technique that has been used throughout history to secure the confidentiality of information. It is a form of linear substitution cipher that employs a mathematical function to transform characters from the original message into encrypted characters. The mathematical formula used in the Affine cipher is:

E(x)=(ax+b) mod m

where:
- E(x) is the encrypted character
- x is the original chracter
- a and b are the encryption keys
- m is the size of the alphabet

The security of the cipher depends on the proper choice of keys


### How the program works

The developed program implements the Affine encryption and decryption. Here is a brief description of each function:

encrypt_affine(message, key1, key2)
This function takes a message and two keys (key1 and key2) as input and returns the encrypted message using the Affine cipher. It converts each character of the original message into an encrypted character according to the formula mentioned above.

decrypt_affine(message, key1, key2)
This function performs the reverse process and decrypts an encrypted message using the keys key1 and key2. It reverses the transformation applied during encryption to obtain the original message.

modular_inverse(a, m)
This function calculates the modular multiplicative inverse of a modulo m. It is used in the Affine decryption process.


### How to run the program?
`python affine_cipher.py`