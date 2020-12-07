from unittest import TestCase
from Card__Game.Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card(2, "Diamond")  # Lowest card.
        self.card2 = Card(1, "Club")     # Highest card.
        self.card3 = Card(12, "Club")    # Random value, highest suit.
        self.card4 = Card(3, "Diamond")  # Random value, lowest suit.
        self.card5 = Card(2, "Heart")    # Lowest value, random suit.
        self.card6 = Card(1, "Spade")    # Highest value, random suit.
        self.card7 = Card(12, "Spade")   # Random card.

    def test___repr__(self):
        self.assertEqual(self.card1.__repr__(), 'Two of Diamonds')

    def test___eq__(self):
        card_test = self.card1
        self.assertTrue(self.card1 == card_test)    # Equal Cards.
        self.assertFalse(self.card1 == self.card5)  # Equal Value.
        self.assertFalse(self.card1 == self.card4)  # Equal Suit.
        self.assertFalse(self.card1 == self.card6)  # Different Value & Suit.

    def test___gt__(self):
        card_test = self.card1
        self.assertFalse(self.card1 > card_test)  # Equal Cards.
        self.assertTrue(self.card7 > self.card3)  # Equal Value.
        self.assertTrue(self.card4 > self.card1)  # Equal Suit.
        self.assertTrue(self.card4 > self.card5)  # Different Value & Suit.
        # Ace Tests:
        self.assertTrue(self.card2 > self.card3)
        self.assertFalse(self.card1 > self.card6)

    def test_invalidValue(self):
        with self.assertRaises(KeyError):
            self.card1.__init__(14, "Diamond")
            self.card1.__init__('Two', "Diamond")
            self.card1.__init__(-2, "Diamond")
            self.card1.__init__(2, 1)
            self.card1.__init__(2, "Test")
            self.card1.__init__(2, "diamond")
