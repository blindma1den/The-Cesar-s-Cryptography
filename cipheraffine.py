# Developed by S4int. Inspired by blindma1den.

# Note: Ciphertext will always be UPPERCASE and Plaintext will always be lowercase

# Define the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Encryption Function
def encrypt_affine(message, key1, key2):
    """
    Encrypts a message using the Affine cipher.
    
    Args:
        message: The message to encrypt.
        key1: The first key for the cipher (multiplier).
        key2: The second key for the cipher (additive constant).

    Returns:
        The encrypted message.
    """
    original_message = message
    encrypted_message = ""
    message = message.lower()
    for letter in message:
        letter_position = alphabet.find(letter)
        #Apply Affine Cipher Formula
        new_position = letter_position * key1 + key2
        new_letter = alphabet[new_position % len(alphabet)]
        encrypted_message += new_letter
    return encrypted_message.upper()

# Decryption Function
def decrypt_affine(message,key1, key2):
    """
    Decrypts a message using the Affine cipher.
    
    Args:
        message: The message to decrypt.
        key1: The first key for the cipher (multiplier).
        key2: The second key for the cipher (additive constant).

    Returns:
        The decrypted message.
    """
    original_message = message
    decrypted_message = ""
    message = message.lower()
    for letter in message:
        letter_position = alphabet.find(letter)
        # Invert the key1 using its modular multiplicative inverse
        multiplicative_inverse = modular_inverse(key1, len(alphabet))
        new_position = (multiplicative_inverse * (letter_position - key2)) % len(alphabet)
        new_letter = alphabet[new_position]
        decrypted_message += new_letter
    return decrypted_message.lower()
        
# Function to calculate the modular multiplicative inverse 
def modular_inverse(a, m):
    """
    Calculates the modular multiplicative inverse of a modulo m.
    
    Args:
        a: The number to find the modular multiplicative inverse of.
        m: The modulo.
        
    Returns:
        The modular multiplicative inverse of a modulo m, or None if it doen't exist.
    """
    # Implementation of Extended Euclidean Algorithm for finding modular inverse.
    def egcd(a,b):
        """
        Extended Euclidean Algorithm to find the greatest common divisor and the modular inverse coefficients.
        """
        if a == 0:
            return (b,0,1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
        
    # Calculate the gcd and the coefficients
    g, x, y = egcd(a, m)
    if g != 1:  
        return None # The modular inverse doesn't exist
    else:
        return x % m # Modular inverse found
# Some Driver Code   
def main():
    options = {
        "encrypt_affine": encrypt_affine,
        "decrypt_affine": decrypt_affine	
    }
    option = input ("What do you want to do? (encrypt/decrypt): ")
    if option.isupper():
        option = option.lower()
    option += "_affine"
    
    if option in options:
        message = input("Enter your message: ")
        key1 = int(input("Enter your first key(multiplier): "))
        key2 = int(input("Enter your second key(additive constant): "))
        message_result = options[option](message, key1, key2)
        print(f"Result: {message_result}")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
        