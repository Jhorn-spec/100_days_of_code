# def prime_checker(number):
#     is_prime = True
#     for i in range(2,number-1):
#         if number%i == 0:
#             is_prime = False
#     if is_prime:
#         print('It is a prime number')
#     else:
#         print("It is not a prime nunber.")

# prime_checker(11)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    text_encode = ""
    for letter in plain_text.lower():
        if direction == 'encode':
            position = alphabets.index(letter)
            new_position = position + shift_amount
            new_letter = alphabets[new_position]
            text_encode += new_letter
        elif direction == 'decode':
            position = alphabets.index(letter)
            new_position = position - shift_amount
            new_letter = alphabets[new_position]
            text_encode += new_letter
    print(f"The encoded text is {text_encode}")


encrypt(plain_text=text, shift_amount=shift)