from unittest import TestCase
from Card__Game.Card import Card
from Card__Game.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck1 = DeckOfCards()

    def test_start(self):  # Testing the startup of a new deck.
        self.assertEqual(type(self.deck1), DeckOfCards)
        self.assertEqual(len(self.deck1.deck), 52)
        for i in range(len(self.deck1.deck)):  # Testing that no card appears twice.
            count = self.deck1.deck.count(self.deck1.deck[i])
            self.assertEqual(count, 1)

    def test_show(self):
        self.assertEqual(self.deck1.show(), None)

    def test_shuffle(self):  # Testing the shuffle() function.
        self.assertNotEqual(self.deck1, self.deck1.shuffle())
        self.assertEqual(len(self.deck1.deck), 52)

    def test_deal_one_valid(self):  # Testing the deal_one() function with valid values.
        card1 = self.deck1.deal_one()
        self.assertEqual(type(card1), Card)
        self.assertNotIn(card1, self.deck1.deck)
        self.assertEqual(len(self.deck1.deck), 51)

    def test_empty_deck(self):  # Testing different functions with an empty deck.
        for i in range(52):
            self.deck1.deal_one()
        self.assertEqual(self.deck1.shuffle(), None)
        self.assertEqual(self.deck1.deal_one(), None)

    def test_funcs_invalid(self):  # Testing different functions with wrong arguments.
        with self.assertRaises(TypeError):
            self.deck1.deal_one("test")
            self.deck1.shuffle("test")
            self.deck1.show("test")
