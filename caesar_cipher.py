alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", 
"i", "j", "k","l","m", "n", "o", "p", "q", "r", "s", "t","u","v", "w", "x", "y", "z"]

def caesar(input_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >= 26:
                new_position -= 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"The input is {input_text} and cipher text is {cipher_text}")

from art import logo
print(logo)

game_is_end = False
while not game_is_end:
    direction = input("Type 'Encode' to encrypt, tpe'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shiff number:\n"))
    shift  = shift % 26

    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Do you want cipher another text?\nY/n?")
    if restart == "n":
        game_is_end = True
        print("Goodbye")