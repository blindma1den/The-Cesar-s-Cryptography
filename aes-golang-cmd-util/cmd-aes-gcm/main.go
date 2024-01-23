package main

import (
	"bufio"
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"encoding/base64"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
)

const (
	default_key_aes = "Bl1ndma1denChall" //aes128
)

func EncryptAESGCM(key []byte, plaintext []byte) []byte {	
	block, err := aes.NewCipher(key)
	if err != nil {
		log.Fatal("Error creando Cipher:", err)
	}

	//Craer nuevo GCM
	aesGCM, err := cipher.NewGCM(block)
	if err != nil {
		log.Fatal("Error creando CGM:", err)
	}

	//Crear a "nonce".
	nonce := make([]byte, aesGCM.NonceSize())
	if _, err = io.ReadFull(rand.Reader, nonce); err != nil {
		log.Fatal("Error creando Nonce:", err)
	}

	//Encrypt aesGCM.Seal
	ciphertext := aesGCM.Seal(nonce, nonce, plaintext, nil)
	return ciphertext
}

func DecryptAESGCM(key []byte, enc []byte) []byte {
	block, err := aes.NewCipher(key)
	if err != nil {
		log.Fatal("Error creando Cipher:", err)
	}

	//Create a new GCM
	aesGCM, err := cipher.NewGCM(block)
	if err != nil {
		log.Fatal("Error creando GCM:", err)
	}

	//Nonce size 
	nonceSize := aesGCM.NonceSize()

	//Recupero el Nonce del texto cifrado
	nonce, ciphertext := enc[:nonceSize], enc[nonceSize:]

	plaintext, err := aesGCM.Open(nil, nonce, ciphertext, nil)
	if err != nil {
		panic(err.Error())
	}
	return plaintext
}

func ReadPipe() []byte {
	pipe := bufio.NewScanner(os.Stdin)
	pipe.Split(bufio.ScanLines)
	pipe.Scan() //solo primer linea "\n"
	text := []byte(pipe.Text())
	return text
}

func main() {
	encode := flag.Bool("encode", false, "Encriptar texto desde input pipe")
	decode := flag.Bool("decode", false, "Desencriptar texto desde input pipe")
	key := flag.String("key", "", "Key para AES. El largo define AES-128, AES-192 o AES-256 ")
	flag.Parse()

	keyaes := default_key_aes
	if len(*key) > 0 {
		if len(*key) == 16 || len(*key) == 24 || len(*key) == 32 {
			keyaes = *key
		} else {
			log.Fatal("Longitud de la Key tiene que ser 16, 24 o 32 bytes.")
		}
	}

	pipetext := ReadPipe()
	if *encode {
		out := EncryptAESGCM([]byte(keyaes), pipetext)
		//fmt.Println(hex.EncodeToString(out))
		fmt.Println(base64.StdEncoding.EncodeToString(out))
	}

	if *decode {
		enc, err := base64.StdEncoding.DecodeString(string(pipetext))
		if err != nil {
			log.Fatal("Texto en base64 Invalido: ", err)
		}
		out := DecryptAESGCM([]byte(keyaes), enc)
		fmt.Println(string(out))
	}

	if !*encode && !*decode {
		fmt.Printf("%s\n\n", "Error: Opcion invalida o sin parametros.")
		flag.PrintDefaults()
	}

}
