def ceaser(input_text,shift_amount,shift_direction):
    final_text=""
    if shift_direction=="decode":
            shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter= alphabet[new_position]
            final_text += new_letter
        else:
            final_text += char
    print(f"The {shift_direction}d text is {final_text}")

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end_check= False
while not end_check:
    
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    ceaser(text,shift,direction)
    
    repeat= input("Do you want to continue? Yes or No \n").lower()
    if repeat=="no":
        end_check=True

# def encrypt(plain_text, shift_amount):
#     cypher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cypher_text += new_letter
#     print(f"The encoded text is : {cypher_text}")

# def decode(plain_text, shift_amount):
#     decoded_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decoded_text += new_letter
#     print(f"The Decoded Text is : {decoded_text}")


# if direction == "encode":
#     encrypt(text,shift)
# else:
#     decode(text,shift)


        
ceaser(text,shift,direction)