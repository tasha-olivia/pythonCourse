alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ceaser cipher
def ceasar(plain_text, shift_amount, to_do):
    output_phrase = ""
    for character in plain_text:
        if character in alphabet:
            index = alphabet.index(character)
            if to_do == "encode":
                new_index = index + shift_amount
            elif to_do == "decode":
                new_index = index - shift_amount
            word = alphabet[new_index]
        else:
            word = character
        output_phrase += word
    print(f"The {to_do}d message is {output_phrase} ")

run_again = "yes"
while run_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    ceasar(plain_text=text,shift_amount=shift,to_do=direction)
    run_again = input("Type 'yes' if you want to run the cipher game again else type no: \n").lower()
print("Good Bye")