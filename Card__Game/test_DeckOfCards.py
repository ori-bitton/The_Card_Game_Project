from unittest import TestCase
from Card__Game.Card import Card
from Card__Game.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck1 = DeckOfCards()
        self.deck2 = DeckOfCards()
        self.deck2.deck = []

    def test_start(self):  # Testing the startup of a new deck.
        self.assertEqual(type(self.deck1), DeckOfCards)
        self.assertEqual(len(self.deck1.deck), 52)
        for i in range(len(self.deck1.deck)):  # Testing that no card appears twice.
            count = self.deck1.deck.count(self.deck1.deck[i])
            self.assertEqual(count, 1)

    def test_shuffle(self):  # Testing the shuffle() function.
        copy_deck1 = self.deck1.deck[:]
        self.deck1.shuffle()
        copy_deck2 = self.deck2.deck[:]
        self.deck2.shuffle()
        self.assertNotEqual(self.deck1.deck, copy_deck1)  # Shuffling will change the deck list.
        self.assertEqual(len(self.deck1.deck), 52)        # but won't change the number of cards.
        self.assertEqual(self.deck2.deck, copy_deck2)     # Shuffling an empty deck will change nothing.

    def test_deal_one(self):  # Testing the deal_one() function.
        card1 = self.deck1.deal_one()
        self.assertEqual(type(card1), Card)
        self.assertNotIn(card1, self.deck1.deck)
        self.assertEqual(len(self.deck1.deck), 51)
        self.assertEqual(self.deck2.deal_one(), None)  # Taking a card from an empty deck won't return anything.

    def test_funcs_invalid(self):  # Testing different functions with wrong arguments.
        with self.assertRaises(TypeError):
            self.deck1.deal_one("test")
            self.deck1.shuffle("test")
            self.deck1.show("test")
