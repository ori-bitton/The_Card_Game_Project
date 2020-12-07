from Card__Game.Card import Card
from Card__Game.DeckOfCards import DeckOfCards
from random import randint


class Player:

    def __init__(self, name, numofcards=10):
        self.name = str(name)
        self.numofcards = numofcards
        if self.numofcards > 26 or self.numofcards < 0:
            raise IndexError("A player's deck has to be between 0 and 26")
        self.playerdeck = []

    def set_hand(self, maindeck):  # Set the player's hand.
        if type(maindeck) == DeckOfCards:
            for i in range(self.numofcards):
                self.playerdeck.append(maindeck.deal_one())
        else:
            raise TypeError("set_hand function must receive a DeckOfCards.")

    def get_card(self):  # Take a card from the player.
        if self.playerdeck != 0:
            self.numofcards -= 1
            return self.playerdeck.pop(randint(0, self.numofcards))
        else:
            print("Player has no Cards.")

    def add_card(self, card):  # The player adds a card to his hand.
        if type(card) != Card:
            raise TypeError("Invalid Type, Must be Card.")
        self.playerdeck.append(card)
        self.numofcards += 1

    def show(self):  # SHows the player's details: Name, Cards & Number of cards.
        print(self.name)
        print(f"{self.playerdeck} ({self.numofcards} Cards)")

    def __gt__(self, other):
        if len(self.playerdeck) > len(other.playerdeck):
            return True
        if len(self.playerdeck) < len(other.playerdeck):
            return False

    def __eq__(self, other):
        if len(self.playerdeck) == len(other.playerdeck):
            return True
        else:
            return False