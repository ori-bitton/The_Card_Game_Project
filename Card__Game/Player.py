from Card__Game.Card import Card


class Player:

    def __init__(self, name, numofcards=10):
        self.name = str(name)
        self.numofcards = numofcards
        if self.numofcards > 26:
            self.numofcards = 26
        self.playerdeck = []

    def set_hand(self, maindeck):
        for i in range(self.numofcards):
            self.playerdeck.append(maindeck.deal_one())

    def get_card(self):
        if self.playerdeck != 0:
            self.numofcards -= 1
            return self.playerdeck.pop()
        else:
            print("Player has no Cards.")

    def add_card(self, card):
        if type(card) != Card:
            raise TypeError("Invalid Type, Must be Card.")
        self.playerdeck.append(card)
        self.numofcards += 1

    def show(self):
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