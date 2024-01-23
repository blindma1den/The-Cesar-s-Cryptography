package main

import (
	"bufio"
	"crypto/aes"
	"encoding/base64"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

const (
	default_key_aes = "Bl1ndma1denChall" //aes128
	padding_for_aes = "."
)

func EncryptAES(key []byte, plaintext []byte) []byte {
	c, err := aes.NewCipher(key)
	if err != nil {
		log.Fatal("Error creando Cipher:", err)
	}
	out := make([]byte, aes.BlockSize)
	c.Encrypt(out, plaintext)
	return out
}

func DecryptAES(key []byte, ciphertext []byte) []byte {
	c, err := aes.NewCipher(key)
	if err != nil {
		log.Fatal("Error creando Cipher:", err)
	}
	pt := make([]byte, aes.BlockSize)
	c.Decrypt(pt, ciphertext)
	return pt
}

func ReadPipe(decodehex bool) []byte {
	pipe := bufio.NewScanner(os.Stdin)
	pipe.Split(bufio.ScanLines)
	pipe.Scan() //solo primer linea "\n"
	text := []byte(pipe.Text())
	if decodehex {
		//text, _ = hex.DecodeString(pipe.Text())
		text, _ = base64.StdEncoding.DecodeString(pipe.Text())
	}
	if len(text) < 16 {
		padd := strings.Repeat(padding_for_aes, 16-len(text))
		text = append(text, padd...)
	}
	if len(text) > 16 {
		text = text[:16]
	}

	return text

}

func main() {
	encode := flag.Bool("encode", false, "Encriptar texto desde input pipe")
	decode := flag.Bool("decode", false, "Desencriptar texto desde input pipe")
	key := flag.String("key", "", "Key para AES. El largo define AES-128, AES-192 o AES-256 ")
	flag.Parse()

	//Si el comando "-key" no esta definido
	//se utiliza la default key
	//Si esta definida la key, pero
	//el largo de la key no es 16,24 o 32
	//muestra error.
	keyaes := default_key_aes
	if len(*key) > 0 {
		if len(*key) == 16 || len(*key) == 24 || len(*key) == 32 {
			keyaes = *key
		} else {
			log.Fatal("Longitud de la Key tiene que ser 16, 24 o 32 bytes.")
		}
	}

	pipetext := ReadPipe(*decode)
	if *encode {
		out := EncryptAES([]byte(keyaes), pipetext)
		//fmt.Println(hex.EncodeToString(out))
		fmt.Println(base64.StdEncoding.EncodeToString(out))
	}

	if *decode {
		out := DecryptAES([]byte(keyaes), pipetext)
		fmt.Println(string(out))
	}

	if !*encode && !*decode {
		fmt.Printf("%s\n\n", "Error: Opcion invalida o sin parametros.")
		flag.PrintDefaults()
	}

}
