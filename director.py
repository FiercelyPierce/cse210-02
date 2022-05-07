'''

'''
import random
from deck import Deck

# cse210
# Team 4 - Spring2022
# 
# Pierce Cirks
# Matthew Scoville
# Anita Taylor
# Andrew Vargas

print()
user_points = 300

class Director:

    # Loop the game until user get 0 points
    def main(self):
        while user_points > 0:
            self.guess()
            
        print("Game over")
        

    # Prompts the player to guess whether the next number will be Higher (H), or Lower (L)    
    def guess(self):
        card_number = Deck.drawCard()
        print(f"The card is {card_number}")
        user_choice = input("Higher or lower (H/L)  ")
        next_number = Deck.drawCard()
        print(f"Next card was: {next_number}")

        if next_number > card_number and user_choice.lower() == "h":
            self.correct_asnwer()
        elif next_number < card_number and user_choice.lower() == "h":
            self.incorrect_answer()
        elif next_number < card_number and user_choice.lower() == "l":
            self.correct_asnwer()
        elif next_number > card_number and user_choice.lower() == "l":
            self.incorrect_answer()
        else:
            print("There seems to be a typo. Please try again")


    # Calculates the current points the player has
    def correct_asnwer(self):
        new_points = user_points + 100
        print(f"your score is {new_points}")
        print()


    def incorrect_answer(self):
        new_points = user_points - 75
        print(f"your score is {new_points}")
        print()


    main()
