import string
from logo import ceaser_logo

print(ceaser_logo)

alphabet = list(string.ascii_letters)

def caeser(original_text, shift_amount, encode_or_decode):
    ciper = ""
    if encode_or_decode == "decode":
                shift_amount *= -1
    for letter in original_text:

        if letter not in original_text:
            ciper += letter
        else:
            shifted_position =  alphabet.index(letter) + shift_amount

            # to prevent index going out of range
            shifted_position %= len(alphabet)
            ciper += alphabet[shifted_position]

    print(f"The {encode_or_decode}d is {ciper}")

keep_going = True

while keep_going:

    direction = input("Enter 'encode' to encode and 'decode' to decode the string:\n").lower()
    text = input("Enter the word you want to decode or encode:\n")
    shift = int(input("Enter the number of shift you want to execute:\n"))

    caeser(original_text = text , shift_amount = shift, encode_or_decode = direction)    

    run_again = input("Do you want to rerun the program? Type 'yes' or 'no' ").lower()

    if run_again == "no":
        keep_going = False
    print("Good Bye!")    
    
