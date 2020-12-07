from Card__Game.DeckOfCards import DeckOfCards
from Card__Game.CardGame import CardGame

deck = DeckOfCards()
game = CardGame('Player 1', 'Player 2', deck)

game.player1.show()
game.player2.show()

for i in range(10):
    player1_card = game.player1.get_card()
    player2_card = game.player2.get_card()
    if player1_card > player2_card:
        game.player2.add_card(player1_card)
        game.player2.add_card(player2_card)
        print(f"Round {i+1} Winner:")
        game.player1.show()
        print(f"Cards thrown: {player1_card}, {player2_card}.")
    elif player2_card > player1_card:
        game.player1.add_card(player1_card)
        game.player1.add_card(player2_card)
        print(f"Round {i + 1} Winner:")
        game.player2.show()
        print(f"Cards thrown: {player1_card}, {player2_card}.")

winner = game.get_winner()
if winner is None:
    print("Game Draw")
else:
    print(f"Game Winner: ")
    winner.show()
