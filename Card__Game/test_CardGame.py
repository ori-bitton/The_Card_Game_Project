from unittest import TestCase
from Card__Game.CardGame import CardGame
from Card__Game.Player import Player
from Card__Game.DeckOfCards import DeckOfCards


class TestCardGame(TestCase):

    def setUp(self):
        self.deck1 = DeckOfCards()
        self.game1 = CardGame('Amit', 'Ori', self.deck1, 20)

    def test_new_game(self):
        self.assertNotEqual(self.deck1.deck, self.game1.deck)
        self.assertEqual(len(self.game1.player1.playerdeck), 20)
        self.assertEqual(len(self.game1.player2.playerdeck), 20)
        for i in range(20):
            self.assertNotIn(self.game1.player1.playerdeck[i], self.deck1.deck)
            self.assertNotIn(self.game1.player2.playerdeck[i], self.deck1.deck)
        with self.assertRaises(ReferenceError):
            self.game1.new_game()

    def test_get_winner(self):
        self.game1.player2.get_card()
        self.assertNotEqual(self.game1.player1.playerdeck, self.game1.player2.playerdeck)
        self.assertEqual(self.game1.get_winner(), self.game1.player2)
