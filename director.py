'''

'''
import random
from deck import ____


'''def main():
    current_points = calculate_points()

    # Runs the program until the player either runs out of points or cards
    while current_points > 0 and ____:
        pass

# Calculates the current points the player has
def calculate_points():
    pass    

# Prompts the player to guess whether the next number will be Higher (H), or Lower (L)
def guess_prompt():
    pass
'''

print()
user_points = 300
card = [1,2,3,4,5,6,7,8,9,10,11,12,13]


 # Loop tha game until user get 0 points
def main():
    while user_points != 0:
        guess()
    print("Game over")


# Prompts the player to guess whether the next number will be Higher (H), or Lower (L)
def guess():
    card_number = random.choice(card)
    print(f"The card is {card_number}")
    user_choise = input("Higher or lower (h/l)  ")
    next_number = random.choice(card)
    print(f"Next card was: {next_number}")

    if next_number > card_number and user_choise == "h":
        correct_asnwer()
    elif next_number < card_number and user_choise == "h":
        incorrect_answer()
    elif next_number < card_number and user_choise == "l":
        correct_asnwer()
    elif next_number > card_number and user_choise == "l":
        incorrect_answer()
    else:
        print("Try again")


# Calculates the current points the player has
def correct_asnwer():
    correct = user_points + 100
    new_points = correct
    print(f"your score is {new_points}")
    print()


def incorrect_answer():
    incorrect = user_points - 75
    new_points = incorrect
    print(f"your score is {new_points}")
    print()
main()
