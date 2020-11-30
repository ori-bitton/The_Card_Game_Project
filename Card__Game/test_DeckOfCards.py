from unittest import TestCase
from Card__Game.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck1 = DeckOfCards()

    def test_show(self):
        self.assertEqual(self.deck1.show(), print(self.deck1.deck))

    def test_shuffle(self):
        self.assertNotEqual(self.deck1, self.deck1.shuffle())

    def test_deal_one(self):
        pass
