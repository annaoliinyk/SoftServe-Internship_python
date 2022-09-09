# Task from https://exercism.org/tracks/python/exercises/pangram
import logging

logging.basicConfig(level=logging.INFO)

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def is_pangram(sentence: str):
    try:
        sentence = sentence.lower()
        for letter in ALPHABET:
            if letter not in sentence:
                return False
        return True
    except:
        logging.error('Invalid input')


def main():
    logging.info(is_pangram('a quick movement of the enemy will jeopardize five gunboats'))
    logging.info(is_pangram("The quick brown fox jumps over a lazy dog"))
    logging.info(is_pangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'))
    logging.info(is_pangram('Five quacking Zephyrs jolt my wax bed.'))
    logging.info(is_pangram('abcdefghijklmnopqrstuvwxy'))


if __name__ == '__main__':
    main()
