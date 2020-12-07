from unittest import TestCase
from Card__Game.Player import Player
from Card__Game.DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.player1=Player("Amit")
        self.player2=Player("Ori")
        self.maindeck=DeckOfCards()
        print("SetUp")

    def tearDown(self):
        print("TearDown")

    def test_set_hand(self):
        #Both players need to take their cards from the same deck
        self.player1.set_hand(self.maindeck)
        self.player2.set_hand(self.maindeck)
        self.assertEqual(len(self.maindeck.deck), 32)

        #Players deck length needs to be equal to numofcards
        self.assertEqual(len(self.player1.playerdeck), self.player1.numofcards)
        self.assertEqual(len(self.player2.playerdeck), self.player2.numofcards)

    def test_get_card(self):
        #The function takes a card from the player and presents it
        self.player1.set_hand(self.maindeck)
        self.player1.get_card()
        self.assertEqual(len(self.player1.playerdeck),self.player1.numofcards)

        #Edge Cases
        with self.assertRaises(IndexError):
            self.player2.get_card()
            self.player1.numofcards=-1

    def test_add_card(self):
        #The function adds a cards from the main deck to the player deck.
        self.player1.set_hand(self.maindeck)
        self.player1.add_card(self.maindeck)
        self.assertEqual(len(self.player1.playerdeck),self.player1.numofcards)
        self.assertEqual(len(self.maindeck.deck), 41)