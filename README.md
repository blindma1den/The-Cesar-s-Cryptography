# The Vigenere Cipher.

***EN.***</br>
This Bash Script allows users to encrypt messages using the Vigenere's cipher.

### What is the Vigenere Cipher?
The Vigenère cipher is a cipher based on different series of characters or letters of the Caesar cipher, these characters forming a table, called the Vigenère table, which is used as a key. The Vigenère cipher is a polyalphabetic and substitution cipher.

### ***How does it work?*** </br>
First, we need to know that the Alphabet could be used in two ways:
```
1. a=0, b=1, c=2...
2. a=1, b=2, c=3...

```
If we use the first way, where the Alphabet starts its index by A=0, we could do the method in a piece of paper and a pencil and encrypt the message.

Choose a type of alphabet. In this case, the one that starts by 0.
```
A0-B1-C2-D3-E4-F5-G6-H7-I8-J9-K10-L11-M12-N13-O14-P15-Q16-R17-S18-T19-U20-V21-W22-X23-Y24-Z25
```
Each letter/character in the Alphabet has a number assigned to it. You have to know which number corresponds to each character.

Choose a Message to encrypt, and then a Key.  
MESSAGE: RETOCIBERSEGURIDAD  
KEY: DISCORD     
  
Now, we locate the numbers or characters of each one:  
R17-E4-T19-O14...  
The same with the key:
D3-I8-S18-C2-O14-R17-D3

Once we have the numbers and characters, we will have to obtain the result of the sum between the numbers of each character between the Message and the Key.  
```
R17 - D3: 17 + 3: 20 corresponds to character U.
```  
In this way you will encrypt the whole message.  

### What if the message is longer than the key? Simple:  
The key is repeated as many times as necessary to cover the entire length of the message:  
```
before:
RETOCIBERSEGURIDAD
DISCORD

after:
RETOCIBERSEGURIDAD
DISCORDDISCORDDISC
```  
But, the Alphabet ends in Z, which corresponds to the number 25 in this case.  
  
### What if the sum exceeds this number Z-25? Would the character be left out of the alphabet?  
You do MOD-26 operation with the result of the sum  
  
Example:  
Z25 + D3 = 28-???  
28 MOD 26 = 2. And 2 corresponds to the letter C.  
  
This way we maintain control over the alphabet and their characters and numbers.  



REFERENCES:
Vigenere Cipher: https://www.ugr.es/~anillos/textos/pdf/2010/EXPO-1.Criptografia/02a11.htm
