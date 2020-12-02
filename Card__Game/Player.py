from Card__Game.DeckOfCards import DeckOfCards


class Player:

    def __init__(self, name, numofcards=10):
        self.name = str(name)
        self.numofcards = numofcards
        if self.numofcards > 26:
            self.numofcards = 26
        self.playerdeck = []

    def set_hand(self, maindeck):
        if maindeck != DeckOfCards():
            raise TypeError("Invalid Type, Must be DeckOfCards.")
        for i in range(self.numofcards):
            self.playerdeck.append(maindeck.deal_one())

    def get_card(self):
        self.playerdeck.pop(0)

    def add_card(self, maindeck):
        if maindeck != DeckOfCards():
            raise TypeError("Invalid Type, Must be DeckOfCards.")
        self.playerdeck.append(maindeck.deal_one())

    def show(self):
        print(self.name)
        print(self.playerdeck)

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
