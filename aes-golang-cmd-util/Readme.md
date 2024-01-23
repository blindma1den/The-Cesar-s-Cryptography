# Simple implementation AES in Golang

This is a simple implementation of the AES cipher using the standard library in Go. This command-line utility can be useful for bash scripting via pipelines. 

It has been created for self-educational purposes only.

Feel free to modify!

## About AES (from Wikipedia) TL;DR;

Advanced Encryption Standard (AES) is a symmetric encryption algorithm, designed by two Belgian cryptographers, Joan Daemen and Vincent Rijmen. It was published as a replacement for the Data Encryption Standard (DES) in 2001 and has since become one of the most widely used encryption algorithms due to its robust security features.

AES supports key sizes of 128, 192, or 256 bits, with the most commonly used being 256 bits, which provides a large enough key space to resist brute force attacks for an extended period.

When using AES in encryption mode, it typically involves padding the plaintext before encryption to ensure its length is a multiple of the block size (16 bytes for AES-256), then encrypting the padded plaintext with a unique initialization vector (IV) and key. During decryption, the IV and key are used to undo the encryption process, and the padding is removed before returning the decrypted plaintext.

AES has been widely adopted for securing data both at rest (storage) and in transit (communications), as well as being a standard encryption method for various protocols like SSL/TLS and IPsec. AES also forms the basis for other encryption algorithms, such as Galois/Counter Mode (GCM) and Cipher Block Chaining-MAC Protocol (CBC-MAC).

## About implementation in Go

The main purpose of these utilities is to use them through pipes in bash scripts.

I have provided two examples, one using pure AES encryption and another utilizing AES with Galois/Counter Mode (GCM) without padding.

The pure AES implementation restricts the size of data to be encrypted to a multiple of 16 bytes due to its block cipher nature.

To overcome this limitation in real-world scenarios, a common practice is to use the advanced AES mode - Galois Counter Mode (GCM).". RTFM.

### How to compile and run

For AES: The text to be encrypted must have a length that is a multiple of 16 bytes. If not, it will be padded with spaces or truncated.

```bash
cd cmd-aes
go build -o cmd-aes main.go
echo "text to cipher" | ./cmd-aes -encode
echo "text to cipher" | ./cmd-aes -encode -key "abracadabrapatas"
echo "text to cipher" | ./cmd-aes -encode -key "abracadabrapatas" |./cmd-aes -decode -key "abracadabrapatas"
```

For AES-GCM: No limitations on length.

```bash
cd cmd-aes-gcm
go build -o cmd-aes-gcm main.go
echo "text to cipher" | ./cmd-aes-gcm -encode
echo "text to cipher" | ./cmd-aes-gcm -encode -key "abracadabrapatas"
echo "text to cipher" | ./cmd-aes-gcm -encode -key "abracadabrapatas" |./cmd-aes-gcm -decode -key "abracadabrapatas"
```



## RTFM
https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
https://pkg.go.dev/crypto/aes
https://www.melvinvivas.com/how-to-encrypt-and-decrypt-data-using-aes
https://kashifsoofi.github.io/cryptography/aes-in-go-using-crypto-package/
https://en.wikipedia.org/wiki/Galois/Counter_Mode


## TODO

- Maybe add other block ciphers? CBC?
- More commandlines parameteres?
- Refactoring...
