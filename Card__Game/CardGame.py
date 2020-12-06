from Card__Game.DeckOfCards import DeckOfCards
from Card__Game.Player import Player


class CardGame:

    def __init__(self, name1, name2, deck, hand=10):
        global a
        a = True
        self.deck = deck
        if type(deck) != DeckOfCards:
            raise TypeError("must be DeckOfCards type")
        self.player1 = Player(str(name1), hand)
        self.player2 = Player(str(name2), hand)
        self.new_game()

    def new_game(self):
        global a
        if a is True:
            self.deck.shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
            a = False
        else:
            raise ReferenceError("new_game function may only run in __init__.")

    def get_winner(self):
        if self.player1 > self.player2:
            return self.player1
        elif self.player2 > self.player1:
            return self.player2
        elif self.player1 == self.player2:
            return
