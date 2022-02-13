alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text, shift_amount, direction_type):
  if direction_type == "encode":
    cipher_text = ""
    for letter in plain_text:
      if alphabet.index(letter) >= 20:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
      else:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
  elif direction_type == "decode":
    decoded_text = ""
    for letter in plain_text:
      if alphabet.index(letter) >= 20:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decoded_text += new_letter
      else:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    print(f"The decoded text is {decoded_text}")


caesar(plain_text=text, shift_amount=shift,direction_type=direction)
  