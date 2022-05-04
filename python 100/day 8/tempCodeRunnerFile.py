# encrypt function
# def encrypt(phrase, shift_amount):
#     encoded_word = ""
#     for letter in phrase:
#         if letter == " ": 
#             word = " "
#         else:
#             index = alphabet.index(letter)
#             new_index = index + shift_amount
#             if new_index > 25:
#                 new_position = new_index - 26
#             else:
#                 new_position = new_index
#             word = alphabet[new_position]
#         encoded_word  += word
#     print(f"The encoded text is {encoded_word}")

# # decrypt function
# def decrypt(encoded_message, shift_number):
#     decoded_word = ""
#     for letter in encoded_message:
#         if letter == " ":
#             word = " "
#         else:
#             position = alphabet.index(letter)
#             new_position = position - shift_number
#             word = alphabet[new_position]
#         decoded_word += word 
#     print(f"The decoded word is {decoded_word} ")

# if  direction == "encode":
#     encrypt(phrase=text,shift_amount=shift)
# elif direction == "decode":
#     decrypt(encoded_message=text, shift_number=shift)
# else:
#     print("You entered a  wrong choice")