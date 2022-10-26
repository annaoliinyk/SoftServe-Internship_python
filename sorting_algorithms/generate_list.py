import random


def generate_list(length=8):
    generated_list = []
    for i in range(length):
        random_number = random.randint(0, length * length)
        generated_list.append(random_number)
    return generated_list
