from Card__Game.DeckOfCards import DeckOfCards
from random import randint


class Player:

    def __init__(self, name, numofcards=10):
        self.name = str(name)
        self.numofcards = numofcards
        if self.numofcards > 26 or self.numofcards < 0:
            raise IndexError("A player's deck has to be between 0 and 26")
        self.playerdeck = []

    def set_hand(self, maindeck):
        for i in range(self.numofcards):
            self.playerdeck.append(maindeck.deal_one())

    def get_card(self):
        if self.numofcards<=0:
            raise IndexError("Your deck is already empty.")
        self.numofcards-=1
        return self.playerdeck.pop(randint(0,self.numofcards))

    def add_card(self, maindeck):
        self.playerdeck.append(maindeck.deal_one())
        self.numofcards+=1

    def show(self):
        return f"{self.name}\n{self.playerdeck} ({self.numofcards} Cards)"

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