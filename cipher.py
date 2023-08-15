alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 
           'o', 'p','q','r','s','t','u','v','w','x','y','z','a', 'b', 'c', 'd',
           'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p','q','r',
           's','t','u','v','w','x','y','z']


#METHOD 2
def ceasar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
            shift_amount *= -1  #e.g 5 = 5 * -1 = -5
    for char in start_text:
        #if character is in the alphabet 
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            #else the characters should maintain  
            end_text += char
        
    print(f'The {cipher_direction}d text is {end_text}')
        
should_continue = True
while should_continue:
    
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt.\n")
    text = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number\n"))
    #if a user enter a number larger than 26 let the message be shifted by the remainder
    shift_number = shift_number % 26

    ceasar(start_text=text,shift_amount=shift_number,cipher_direction=direction)
    code_again = input("Type 'yes' if you want to go again or 'no':").lower()
    if code_again != 'yes':
        should_continue =False
        print("Goodbye")



#METHOD 1
""" 
def encrypt(plain_text,shift_amount):
    cipher_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print("The encrypted text is:",cipher_text)

def decrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print("The decrypted text is:",cipher_text)

if direction == 'encode':
    encrypt(plain_text=text,shift_amount=shift_number)
elif direction == 'decode':
    decrypt(plain_text=text,shift_amount=shift_number) 
 """