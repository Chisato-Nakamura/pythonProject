alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(user_choice, plain_text, shift_amount):
    caesar_cipher = ""
    if user_choice == "decode":
        shift_amount *= -1
    elif user_choice != "encode" and user_choice != "decode":
        print("Error - Please try again.")

    for position in plain_text:
        if position in alphabet:
            index = alphabet.index(position)
            move = index + shift_amount
            caesar_cipher += alphabet[move]
        else:
            caesar_cipher += position

    print(f"The decoded text is {caesar_cipher}")


from art import logo

print(logo)

end_of_game = False

while not end_of_game:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(user_choice=direction, plain_text=text, shift_amount=shift)

    restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == 'yes':
        end_of_game = False
    elif restart == 'no':
        end_of_game = True




