from Card__Game.Card import Card
from random import *


class DeckOfCards:

    def __init__(self):
        self.deck = []
        shapes = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}  # New dictionary for creating cards.
        while len(self.deck) < 52:
            new_card = Card(randint(1, 13), shapes[randint(1, 4)])
            if new_card not in self.deck:
                self.deck.append(new_card)

    def show(self):  # Print the cards in the deck.
        print(f"{self.deck}")

    def shuffle(self):  # Shuffle the order of the cards in the deck.
        if len(self.deck) > 0:
            shuffle(self.deck)
        else:
            print("Deck has no Cards.")

    def deal_one(self):  # Deal 1 random card from the deck.
        if len(self.deck) > 0:
            return self.deck.pop(randint(0, len(self.deck)-1))
        else:
            print("Deck has no Cards.")
