from unittest import TestCase
from Card__Game.CardGame import CardGame
from Card__Game.DeckOfCards import DeckOfCards


class TestCardGame(TestCase):

    def setUp(self):
        self.game1 = CardGame('Amit', 'Ori', 20)

    def test_new_game(self):
        self.assertEqual(len(self.game1.player1.playerdeck), 20)  # Testing both players got 20 cards.
        self.assertEqual(len(self.game1.player2.playerdeck), 20)
        for i in range(20):  # Testing no card repeats itself in the deck.
            self.assertNotIn(self.game1.player1.playerdeck[i], self.game1.deck)
            self.assertNotIn(self.game1.player2.playerdeck[i], self.game1.deck)
        with self.assertRaises(ReferenceError):
            self.game1.new_game()  # Testing new_game can't run outside the constructor.

    def test_get_winner(self):
        self.assertEqual(self.game1.get_winner(), None)
        self.game1.player2.get_card()                                  # Taking 1 card from player2.
        self.assertEqual(self.game1.get_winner(), self.game1.player2)  # Player2 won.
        for i in range(3):
            self.game1.player1.get_card()                              # Taking 3 cards from player1.
        self.assertEqual(self.game1.get_winner(), self.game1.player1)  # Player1 won.

    def test_invalid_values(self):  # Testing different functions with wrong arguments.
        with self.assertRaises(TypeError):
            CardGame([1, 2, 3], {1: 10, 2: 20, 3: 30}, 'test')
            self.game1.get_winner('test')
            self.game1.new_game('test')
