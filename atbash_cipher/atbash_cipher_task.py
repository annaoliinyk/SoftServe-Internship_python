# Task from https://exercism.org/tracks/python/exercises/atbash-cipher

import logging

logging.basicConfig(level=logging.INFO)

PLAIN_STR = "abcdefghijklm0123456789nopqrstuvwxyz"
CIPHER_STR = "zyxwvutsrqpon0123456789mlkjihgfedcba"


def encode(plain_text):
    try:
        result = ""
        for symbol in plain_text.lower():
            if len(result) % 5 == 0 and symbol in PLAIN_STR:
                result += " "
            result += if_symbol_in_str(PLAIN_STR, symbol)
        return result
    except:
        logging.error("Invalid input type")


def decode(ciphered_text):
    try:
        result = ""
        for symbol in ciphered_text.lower():
            result += if_symbol_in_str(CIPHER_STR, symbol)
        return result
    except:
        logging.error("Invalid input type")


def if_symbol_in_str(str_to_check, symbol):
    tmp_result = ""
    if symbol in str_to_check:
        index = CIPHER_STR.index(symbol)
        tmp_result += PLAIN_STR[index]
    return tmp_result


def main():
    logging.info(encode("yes"))  # expected: "bvh"
    logging.info(encode("no"))  # expected: "ml"
    logging.info(encode("O M G"))  # expected: "lnt"
    logging.info(decode("vcvix rhn"))  # expected: "exercism"
    logging.info(decode("gvhgr mt123 gvhgr mt"))  # expected: "testing123testing"
    logging.info(encode(1))  # expected: error log
    logging.info(decode(["a", "b"]))  # expected: error log


if __name__ == "__main__":
    main()
