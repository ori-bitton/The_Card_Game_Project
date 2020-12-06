from Card__Game.Card import Card
from Card__Game.DeckOfCards import DeckOfCards
from Card__Game.Player import Player
from Card__Game.CardGame import CardGame


deck1 = DeckOfCards()
game1 = CardGame('ori', 'amit', deck1)
game1.new_game()