# cse210
# Team 4 - Spring2022
# 
# Pierce Cirks
# Matthew Scoville
# Anita Taylor
# Andrew Vargas

class Card:
    """
        Class to represent a playing card

        Attributes:
            suit (S,H,C,D) 
            value 1 - 13 (Aces low)
            card (A,2-10,J,Q,K)
    """

    def __init__(self, suit, value):
        """
            Constructor
            Args: self - instance of Card            
        """
        
        self.card_suit = suit 
               
        match suit:
            case "S":
                self.suit_name = "Spades"
            case "H":
                self.suit_name = "Hearts"
            case "C":
                self.suit_name = "Clubs"
            case "D":
                self.suit_name = "Diamonds"
            case _:
                self.suit_name = "unknown"


        self.card_value = value
        
        match value:
            case 1:
                self.card = "A"
            case 11:
                self.card = "J"
            case 12:
                self.card = "Q"
            case 13:
                self.card = "K"
            case _:
                self.card = str(value)

    def show(self):
        """
            Prints the card
        """

        print(f"{self.card} of {self.suit_name}")

    def getValue(self):
        """
            Returns the numeric value of the card instance
        """
        return self.card_value

    def getCardName(self):
        """
            Returns a string with the card and suit
        """
        return f"{self.card} of {self.suit_name}"

