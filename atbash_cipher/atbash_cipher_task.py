# Task from https://exercism.org/tracks/python/exercises/atbash-cipher

import logging

logging.basicConfig(level=logging.DEBUG)

plain_str = "abcdefghijklm0123456789nopqrstuvwxyz"
cipher_str = "zyxwvutsrqpon0123456789mlkjihgfedcba"


def encode(plain_text):
    try:
        result = ""
        for symbol in plain_text.lower():
            if len(result) % 5 == 0 and symbol in plain_str:
                result += " "
            result += if_symbol_in_str(plain_str, symbol)
        return result
    except:
        logging.error("Invalid input type")


def decode(ciphered_text):
    try:
        result = ""
        for symbol in ciphered_text.lower():
            result += if_symbol_in_str(cipher_str, symbol)
        return result
    except:
        logging.error("Invalid input type")


def if_symbol_in_str(str_to_check, symbol):
    tmp_result = ""
    if symbol in str_to_check:
        index = cipher_str.index(symbol)
        tmp_result += plain_str[index]
    return tmp_result


def main():
    logging.debug(encode("yes"))  # expected: "bvh"
    logging.debug(encode("no"))  # expected: "ml"
    logging.debug(encode("O M G"))  # expected: "lnt"
    logging.debug(decode("vcvix rhn"))  # expected: "exercism"
    logging.debug(decode("gvhgr mt123 gvhgr mt"))  # expected: "testing123testing"
    logging.debug(encode(1))  # expected: error log
    logging.debug(decode(["a", "b"]))  # expected: error log


if __name__ == "__main__":
    main()
