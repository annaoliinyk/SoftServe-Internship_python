# Task from https://exercism.org/tracks/python/exercises/pangram

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def is_pangram(sentence):
    sentence = sentence.lower()
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True


def main():
    print(is_pangram('a quick movement of the enemy will jeopardize five gunboats'))
    print(is_pangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'))
    print(is_pangram('Five quacking Zephyrs jolt my wax bed.'))
    print(is_pangram('abcdefghijklmnopqrstuvwxy'))


if __name__ == '__main__':
    main()
