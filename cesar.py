# Define the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function to encrypt a message
def encrypt(message, key):
  """
  Encrypts a message using the Caesar cipher.

  Args:
    message: The message to encrypt.
    key: The key for the cipher.

  Returns:
    The encrypted message.
  """

  encrypted_message = ""
  for letter in message:
    # Get the position of the letter in the alphabet
    letter_position = alphabet.find(letter)
    # Apply the key
    new_position = letter_position + key
    # Get the new letter
    new_letter = alphabet[new_position % len(alphabet)]
    # Add the new letter to the encrypted message
    encrypted_message += new_letter
  return encrypted_message

# Function to decrypt a message
def decrypt(message, key):
  """
  Decrypts a message using the Caesar cipher.

  Args:
    message: The message to decrypt.
    key: The key for the cipher.

  Returns:
    The decrypted message.
  """

  decrypted_message = ""
  for letter in message:
    # Get the position of the letter in the alphabet
    letter_position = alphabet.find(letter)
    # Apply the inverse key
    new_position = letter_position - key
    # Get the new letter
    new_letter = alphabet[new_position % len(alphabet)]
    # Add the new letter to the decrypted message
    decrypted_message += new_letter
  return decrypted_message

# Program options
options = {
  "encrypt": encrypt,
  "decrypt": decrypt
}

# Get the user's desired option
option = input("What do you want to do? (encrypt/decrypt): ")

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