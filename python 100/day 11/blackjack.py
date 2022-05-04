import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_integer = random.randint(0, 12)
    return cards[random_integer]

deal_card()