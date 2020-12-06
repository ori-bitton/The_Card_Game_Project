from unittest import TestCase
from Card__Game.Card import Card
from Card__Game.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck1 = DeckOfCards()

    def test_start(self):
        self.assertEqual(type(self.deck1), DeckOfCards)
        self.assertEqual(len(self.deck1.deck), 52)
        # repeat test

    def test_shuffle(self):
        self.assertNotEqual(self.deck1, self.deck1.shuffle())
        self.assertEqual(len(self.deck1.deck), 52)

    def test_deal_one_valid(self):
        card1 = self.deck1.deal_one()
        self.assertEqual(type(card1), Card)
        self.assertNotIn(card1, self.deck1.deck)
        self.assertEqual(len(self.deck1.deck), 51)

    def test_funcs_invalid(self):
        self.assertRaises(TypeError, self.deck1.deal_one(), 'test')
        self.assertRaises(TypeError, self.deck1.shuffle(), 'test')
