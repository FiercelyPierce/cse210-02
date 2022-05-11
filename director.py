import random
from deck import Deck

# cse210
# Team 4 - Spring2022
# 
# Pierce Cirks
# Matthew Scoville
# Anita Taylor
# Andrew Vargas


class Director():

    def __init__(self):
        
        self.score = 300
        self.is_playing = True
        self.card_deck = Deck()
        self.next_card = None
        self.this_card = None
        self.hilo = ""

    # Loop the game until user get 0 points
    def start_game(self):
        while self.score > 0:
            self.guess()
            
        print("Game over")
        

    # Prompts the player to guess whether the next number will be Higher (H), or Lower (L)    
    def guess(self):
        card_number = Deck.drawCard(self)
        print(f"The card is {card_number}")
        user_choice = input("Higher or lower (H/L)  ")
        next_number = Deck.drawCard(self)
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
        new_points = self.score + 100
        print(f"your score is {new_points}")
        print()


    def incorrect_answer(self):
        new_points = self.score - 75
        print(f"your score is {new_points}")
        print()
