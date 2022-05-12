import random
from deck import Deck
from card import Card

# cse210
# Team 4 - Spring2022
# 
# Pierce Cirks
# Matthew Scoville
# Anita Taylor
# Andrew Vargas


class Director:

    def __init__(self):
        """
            Constructor - initialize the deck
        
            Args: self - an instance of Deck
        """
        
        self.score = 300
        self.is_playing = True
        self.card_deck = Deck()
        self.next_card = None
        self.this_card = None
        self.hilo = ""


    def start_game(self):
        '''Loop the game until user get 0 points
        '''

        #Display the first card
        self.this_card = self.card_deck.drawCard()
        print()
        print(f"The first card is: {self.this_card.getCardName()}")
        
        self.is_playing = True
        
        while self.is_playing:
            self.guess()
            
        print("Game over")
        print(f"Final score: {self.score}")
        print()
        

    def getGuess(self):
        """Prompts the user for a guess, makes sure the input is legal"""
        
        valid_choice = False
        
        while not valid_choice:
            user_choice = input("Will the next card be Higher or Lower (H/L) [Q to quit]? > ").lower()
            valid_choice = user_choice in ['h','l','q']
            if not valid_choice:
                print("Please enter a valid selection.")

        return user_choice

    def guess(self):
        '''Prompts the player to guess whether the next number will be Higher (H), or Lower (L) 
        '''
        #card_number = self.card_deck.drawCard()
        #print(f"The card is {card_number}")

        #Prompt the player for a guess h/l
        user_choice = self.getGuess()

        #Check to see if they want to stop playing
        if user_choice == 'q':
            self.is_playing = False
            return

        #Draw the next card
        self.next_card = self.card_deck.drawCard()
        print()
        print(f"Card drawn: {self.next_card.getCardName()}")
        
        if self.next_card.getValue() > self.this_card.getValue() and user_choice == "h":
            self.correct_answer()
        elif self.next_card.getValue() < self.this_card.getValue() and user_choice == "h":
            self.incorrect_answer()
        elif self.next_card.getValue() < self.this_card.getValue() and user_choice == "l":
            self.correct_answer()
        elif self.next_card.getValue() > self.this_card.getValue() and user_choice == "l":
            self.incorrect_answer()
        else:
            print("Cards are the same.")

        print(f"Current score: {self.score}")
        print()

        #Stop the game if score reaches 0
        if self.score <= 0:
            self.is_playing = False

        #Move next card to this card
        self.this_card = self.next_card


    def correct_answer(self):
        '''Calculates the current points the player has
        '''
        self.score = self.score + 100


    def incorrect_answer(self):
        """Update points for incorrect answer"""
        self.score = self.score - 75
                
