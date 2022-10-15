hank you and I attached my code below.

import random

random_draw_list = random.sample(range(1, 76), 75)

def generate_card():
    card = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": [],
    }
    min = 1
    max = 15
    for letter in card:
        card[letter] = random.sample(range(min, max), 5)
        min += 15
        max += 15
        if letter == "N":
            card[letter][2] = "X" # free space!
    return card

def print_card(card):

    for letter in card:
        print(letter, end="\t")
        for number in card[letter]:
            print(number, end="\t")
        print("\n")
    print("\n")

def main():
    print("Let's play bingo!")
    card = generate_card()

    print("\nHere is your card:\n")
    print_card(card)
main()
