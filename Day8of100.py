# Day 8 is about making caesar cipher. It works by shifting the alphabet by a shift number to encode
# and vice versa to decode. Combine it with positional arguments exercise.

import string


def single_word_encoder(my_word: str, shift_number: int, cipher_direction: str):  # 1 for encoder, 2 for decoder
    l_alphabet = list(string.ascii_lowercase)
    l_word = list(my_word)
    encoded_word = ""
    if cipher_direction == "decode":
        shift_number *= (-1)

    for index, elem in enumerate(l_word):
        new_index = l_alphabet.index(elem) + shift_number
        new_index = new_index % 26
        if not elem.isalpha():
            encoded_word += elem

        encoded_word += l_alphabet[new_index]

    print(f"Here is the {cipher_direction}d word : {encoded_word}")

    return encoded_word


is_done = False
while not is_done:
    mode = input("Type 'encode' or 'decode' : \n")
    word = input("Type your word : \n").lower()
    shift = int(input("Type the shift number: \n"))

    single_word_encoder(word, shift, mode)

    end_flag = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()
    if end_flag == "no":
        is_done = True
        print("Goodbye!")
