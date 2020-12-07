from unittest import TestCase
from Card__Game.CardGame import CardGame
from Card__Game.DeckOfCards import DeckOfCards


class TestCardGame(TestCase):

    def setUp(self):
        self.deck1 = DeckOfCards()
        self.game1 = CardGame('Amit', 'Ori', self.deck1, 20)

    def test_new_game(self):
        self.assertNotEqual(self.deck1.deck, self.game1.deck)
        self.assertEqual(len(self.game1.player1.playerdeck), 20)
        self.assertEqual(len(self.game1.player2.playerdeck), 20)
        for i in range(20):  # Testing no card repeats itself.
            self.assertNotIn(self.game1.player1.playerdeck[i], self.deck1.deck)
            self.assertNotIn(self.game1.player2.playerdeck[i], self.deck1.deck)
        with self.assertRaises(ReferenceError):
            self.game1.new_game()  # Testing new_game can't run outside the constructor.

    def test_get_winner(self):
        self.assertEqual(self.game1.get_winner(), None)
        self.game1.player2.get_card()
        self.assertEqual(self.game1.get_winner(), self.game1.player2)
        for i in range(3):
            self.game1.player1.get_card()
        self.assertEqual(self.game1.get_winner(), self.game1.player1)

    def test_invalid_values(self):  # Testing different functions with wrong arguments.
        with self.assertRaises(TypeError):
            CardGame([1, 2, 3], {1: 10, 2: 20, 3: 30}, 'test')
            self.game1.get_winner('test')
            self.game1.new_game('test')
