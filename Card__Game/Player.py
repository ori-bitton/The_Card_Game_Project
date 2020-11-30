from DeckOfCards import DeckOfCards
class Player:
    def __init__(self, name ,numofcards=10):
        self.name=str(name)
        self.numofcards=numofcards
        if self.numofcards>26:
            self.numofcards=26
        self.playerdeck=[]

    def set_hand(self):
        maindeck=DeckOfCards()
        for i in range(self.numofcards):
            self.playerdeck.append(maindeck.deal_one())

    def get_card(self):
        self.playerdeck.pop(0)

    def add_card(self):
        maindeck=DeckOfCards()
        self.playerdeck.append(maindeck.deal_one())

    def show(self):
        print(self.name)
        print(self.playerdeck)







