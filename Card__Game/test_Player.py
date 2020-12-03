from unittest import TestCase
from Card__Game.Player import Player,DeckOfCards

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
        self.assertEqual(len(self.player1.playerdeck),self.player1.numofcards)
        self.assertEqual(len(self.player2.playerdeck),self.player2.numofcards)


    def test_get_card(self):
        pass

    def test_add_card(self):
        pass

    def test_show(self):
        pass