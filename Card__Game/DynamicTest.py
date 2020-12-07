from Card__Game.Card import Card
from Card__Game.DeckOfCards import DeckOfCards
from Card__Game.Player import Player
from Card__Game.CardGame import CardGame

player1=Player('Amit')
deck1 = DeckOfCards()
#game1 = CardGame('ori', 'amit', deck1)
player1.set_hand(deck1)
for i in range(11):
    player1.get_card()

