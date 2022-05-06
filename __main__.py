from deck import Deck

# Test the deck
mydeck = Deck()

for i in range(len(mydeck.Cards)):
    card = mydeck.drawCard()
    print(f"Card: {card.getCardName()} Value: {card.getValue()}")