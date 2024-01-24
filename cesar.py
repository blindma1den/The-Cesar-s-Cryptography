# Caesar's cryptography by blindma1den
# Debug by S4int

# Note: Ciphertext will always be UPPERCASE and Plaintext will always be lowercase

# Define the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function to encrypt a message
def encrypt_cesar(message, key):
  """
  Encrypts a message using the Caesar cipher.

  Args:
    message: The message to encrypt.
    key: The key for the cipher.

  Returns:
    The encrypted message.
  """
  original_message = message
  encrypted_message = ""
  # For solving bugs the message must be in lowercase
  message = message.lower()
  for letter in message:
    
    # Get the position of the letter in the alphabet
    letter_position = alphabet.find(letter)
    # Apply the key
    new_position = letter_position + key
    # Get the new letter
    new_letter = alphabet[new_position % len(alphabet)]
    # Add the new letter to the encrypted message
    encrypted_message += new_letter
  return encrypted_message.upper()

# Function to decrypt a message
def decrypt_cesar(message, key):
  """
  Decrypts a message using the Caesar cipher.

  Args:
    message: The message to decrypt.
    key: The key for the cipher.

  Returns:
    The decrypted message.
  """
  original_message = message
  decrypted_message = ""
  # For solving bugs the message must be in lowercase
  message = message.lower()
  for letter in message:
    # Get the position of the letter in the alphabet
    letter_position = alphabet.find(letter)
    # Apply the inverse key
    new_position = letter_position - key
    # Get the new letter
    new_letter = alphabet[new_position % len(alphabet)]
    # Add the new letter to the decrypted message
    decrypted_message += new_letter
  return decrypted_message.lower()
  
# Some Driver Code  
def main():
  # Program options
  options = {
    "encrypt_cesar": encrypt_cesar,
    "decrypt_cesar": decrypt_cesar
  }

  # Get the user's desired option
  option = input("What do you want to do? (encrypt/decrypt): ")
  # For debug purposes
  if option.isupper():
    option = option.lower()
  # Add the _cesar
  option += "_cesar"
  # If the option is valid
  if option in options:
    # Get the message from the user
    message = input("Enter the message: ")
    # Get the key from the user
    key = int(input("Enter the key: "))
    # Apply the desired option
    message_result = options[option](message, key)
    # Print the result
    print("Result:", message_result)

  # If the option is not valid
  else:
    print("Invalid option.")
  
if __name__ == "__main__":
  main()