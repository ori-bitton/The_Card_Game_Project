from unittest import TestCase
from Card__Game.Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card(2, "Diamond")
        self.card2 = Card(12, "Heart")
        self.card3 = Card(12, "Club")

    def tearDown(self):
        pass

    def test___repr__(self):
        self.assertEqual(self.card1.__repr__(), 'Two of Diamonds')
        self.assertEqual(self.card2.__repr__(), 'Queen of Hearts')
        self.assertEqual(self.card3.__repr__(), 'Queen of Clubs')

    def test__eq__(self):
        self.card4 = Card(2, "Diamond")
        self.assertTrue(self.card1 == self.card4)
        self.assertFalse(self.card2 == self.card3)
        self.card4 = Card(10, "Diamond")
        self.assertFalse(self.card1 == self.card4)

    def test_isBigger(self):
        self.assertTrue(self.card1 < self.card2)
        self.assertTrue(self.card2 < self.card3)

    def test_invalidValue(self):
        with self.assertRaises(KeyError):
            self.card1.__init__(14, "Diamond")
            self.card1.__init__('Two', "Diamond")
            self.card1.__init__(-2, "Diamond")
            self.card1.__init__(2, 1)
            self.card1.__init__(2, "Test")
            self.card1.__init__(2, "diamond")


