# Task from https://exercism.org/tracks/python/exercises/atbash-cipher

def encode(plain_text):
    plain_str = "abcdefghijklm0123456789nopqrstuvwxyz"
    cipher_str = "zyxwvutsrqpon0123456789mlkjihgfedcba"
    result = ""
    letters_counter = 0
    for symbol in plain_text.lower():
        if letters_counter == 5 and symbol in plain_str:
            result += " "
            letters_counter = 0
        if symbol in plain_str:
            index = plain_str.index(symbol)
            result += cipher_str[index]
            letters_counter += 1
    return result


def decode(ciphered_text):
    plain_str = "abcdefghijklm0123456789nopqrstuvwxyz"
    cipher_str = "zyxwvutsrqpon0123456789mlkjihgfedcba"
    result = ""
    for symbol in ciphered_text.lower():
        if symbol in cipher_str:
            index = cipher_str.index(symbol)
            result += plain_str[index]
    return result
