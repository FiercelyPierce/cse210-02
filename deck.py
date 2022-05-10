import random
from card import Card

# cse210
# Team 4 - Spring2022
# 
# Pierce Cirks
# Matthew Scoville
# Anita Taylor
# Andrew Vargas

class Deck:
    """
        Class to simulate a deck of cards        
    """

    def __init__(self):
        """
            Constructor - initialize the deck
            Args: self - an instance of Deck
        """

        suits = ["S","H","C","D"]

        self.Cards = []

        #Setup an list of cards
        for suit in suits:
            for i in range(13):
                card = Card(suit,i+1)
                self.Cards.append(card)

        #Shuffle the deck
        self.shuffle()

    def shuffle(self):
        """
            Shuffles the deck
        """
        random.shuffle(self.Cards)

    def drawCard(self):
        """
            Returns the instance of Card
            at the top of the deck
        """
        card = self.Cards.pop()
        return card
