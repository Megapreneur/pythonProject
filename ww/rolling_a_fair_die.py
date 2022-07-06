import random


def roll():
    die = random.randint(1, 6)
    return die


print(roll())